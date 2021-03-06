%global debug_package %{nil}

%if 0%{?el6}
# see https://fedorahosted.org/fpc/ticket/395, it was added to el7
%global mono_arches %{ix86} x86_64 sparc sparcv9 ia64 %{arm} alpha s390x ppc ppc64 ppc64le
%global _monodir %{_prefix}/lib/mono
%global _monogacdir %{_monodir}/gac
%endif

Name:           nuget
Version:        2.8.7
Release:        3%{?dist}
Summary:        Package manager for .Net/Mono development platform
%if 0%{?el6}
License:        ASL
%else
License:        ASL 2.0
%endif
Group:          Development/Libraries
Url:            http://nuget.org/

%global tarballversion %{version}+md510+dhx1.orig
Source0:        http://download.mono-project.com/sources/%{name}/%{name}_%{tarballversion}.tar.bz2
Source1:        nuget-core.pc
Source2:        nuget.sh
Patch0:         nuget-fix_xdt_hintpath
BuildRequires:  mono-devel mono-winfx

ExclusiveArch:  %{mono_arches}

%description
NuGet is the package manager for the Microsoft
development platform including .NET. The NuGet client
tools provide the ability to produce and consume
packages. The NuGet Gallery is the central package
repository used by all package authors and consumers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development package for %{name}

%prep
%setup -qn nuget-git
sed -i "s/\r//g" src/Core/Core.csproj
%patch0 -p1

# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

%build
%{?exp_env}
%{?env_options}

xbuild xdt/XmlTransform/Microsoft.Web.XmlTransform.csproj
xbuild src/Core/Core.csproj /p:Configuration="Mono Release"
xbuild src/CommandLine/CommandLine.csproj /p:Configuration="Mono Release"

%install
%{?env_options}
%{__mkdir_p} %{buildroot}%{_monodir}/nuget
%{__mkdir_p} %{buildroot}%{_libdir}/pkgconfig
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0755 %{SOURCE2} %{buildroot}%{_bindir}/`basename -s .sh %{SOURCE2}`
sed -i -e 's/cli/mono/' %{buildroot}%{_bindir}/*
%{__install} -m0755 src/CommandLine/bin/Release/NuGet.Core.dll %{buildroot}%{_monodir}/nuget/
%{__install} -m0755 xdt/XmlTransform/bin/Debug/Microsoft.Web.XmlTransform.dll %{buildroot}%{_monodir}/nuget/
%{__install} -m0755 src/CommandLine/bin/Release/NuGet.exe %{buildroot}%{_monodir}/nuget/

%files
%if ! 0%{?el6}
%{license} LICENSE.txt
%endif
%{_monodir}/nuget
%{_bindir}/*

%files devel
%{_libdir}/pkgconfig/nuget-core.pc

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.7-2
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.8.7-0
- upgrade to 2.8.7 for MonoDevelop 5.10

* Mon Jul 06 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.8.5-2
- Split pc file into devel subpackage
- Use license macro
- Move pc file to _libdir instead datadir

* Fri Jul 03 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.8.5-1
- Update to 2.8.5
- Move nuget into monodir
- Fix licence

* Wed Jun 03 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.8.3-3
- Fix empty debug_package

* Wed May 20 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.8.3-2
- Use xbuild option to build with mono 4
- Use global insted define

* Thu Apr 16 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.8.3-1
- build with Mono4

* Thu Apr 16 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.8.3-0
- copy from Xamarin nuget spec
