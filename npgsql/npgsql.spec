%define debug_package %{nil}
%if 0%{?el6}
%define mono_arches %ix86 x86_64 ia64 %{arm} sparcv9 alpha s390x ppc ppc64
%endif
%if 0%{?rhel}%{?el6}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%define _monodir %{_prefix}/lib/mono
%define _monogacdir %{_monodir}/gac
%endif

Name:       npgsql
Version:    2.2.3
Release:    1%{?dist}
Summary:    A .Net Data Provider for PostgreSQL

Group:      Development/Languages
License:    MIT
URL:        http://npgsql.projects.pgfoundry.org/
Source0:    http://pgfoundry.org/frs/download.php/3793/Npgsql-%{version}-src.zip
Source1:    npgsql.pc

BuildRequires:  mono-devel

ExclusiveArch: %mono_arches

%description
Npgsql is a .Net Data Provider for PostgreSQL.
It allows you to connect and interact with PostgreSQL server using .NET.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for %{name}.

%prep
%setup -q
# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;


%build
xbuild /property:Configuration=Debug-net45 Npgsql/Npgsql.csproj

%install
%{__mkdir_p} %{buildroot}/%{_monogacdir}/
%{__mkdir_p} %{buildroot}/%{_monodir}/npgsql/
%{__mkdir_p} %{buildroot}/%{_libdir}/pkgconfig

install -p -m0644 %SOURCE1 %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0755 Npgsql/bin/Debug-net45/Npgsql.dll %{buildroot}%{_monodir}/npgsql/

gacutil -i %{buildroot}%{_monodir}/npgsql/Npgsql.dll -f -package npgsql -root %{buildroot}/%{_prefix}/lib

%files
%doc README.md
%{_monogacdir}/*
%{_monodir}/npgsql/Npgsql.dll

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/npgsql.pc

%changelog
* Thu Nov 21 2013 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.2.3-1
- Initial packaging