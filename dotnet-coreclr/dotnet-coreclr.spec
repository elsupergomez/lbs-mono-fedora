%global deliverydir bin/Product/Linux.x64.Release
Name:           dotnet-coreclr
Version:        1.1.0
Release:        1%{?dist}
Summary:        .NET Core is a general purpose managed framework

Group:          Development/Languages
License:        MIT
URL:            https://dotnet.github.io/
Source0:        https://github.com/dotnet/coreclr/archive/v%{version}.tar.gz
# otherwise that file is missing semicolons
Source1:        dotnet-coreclr-GeneratedAssemblyInfo.cs
Source2:        xbuild.build
Patch0:         dotnet-coreclr-build.patch
Patch1:         dotnet-coreclr-corelib.patch
Patch2:         dotnet-coreclr-ref.patch
Patch3:         dotnet-coreclr-facade.patch
Patch4:         dotnet-coreclr-fixclang39.patch
# backported patches
Patch10:        dotnet-coreclr-minmaxmacros.patch

BuildRequires:  which
BuildRequires:  make
BuildRequires:  nant
BuildRequires:  cmake
BuildRequires:  llvm
BuildRequires:  clang
BuildRequires:  lldb
BuildRequires:  lldb-devel
BuildRequires:  gettext
BuildRequires:  libicu-devel
BuildRequires:  libcurl-devel
BuildRequires:  libunwind-devel
BuildRequires:  lttng-ust-devel
BuildRequires:  libuuid-devel
BuildRequires:  uuid-devel
BuildRequires:  mono-devel >= 4.4

%description
.NET Core is a set of runtime, library and compiler components.
You can create .NET Core apps that run on multiple OSes and CPUs.

%prep
%setup -q -n coreclr-%{version}
#%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch10 -p1

#TODO: https://github.com/dotnet/coreclr/issues/8016
# error: binding dereferenced null pointer to reference has undefined behavior

cp %{SOURCE2} .
# workaround for a problem that the semicolons for the using lines are missing
mkdir -p bin/obj/Windows_NT.x64.Release
cp %{SOURCE1} bin/obj/Windows_NT.x64.Release/GeneratedAssemblyInfo.cs

%build

nant generateProjectFiles
sed -i "s#__isMSBuildOnNETCoreSupported=0#__isMSBuildOnNETCoreSupported=1#g" build.sh
# for skipgenerateversion, see https://github.com/dotnet/coreclr/issues/4558
# other option: skipmscorlib
./build.sh skipgenerateversion skipnuget x64 Release clean

%install

# putting the binaries in bin/dotnet, to avoid conflict with mono-devel, ilasm
mkdir -p %{buildroot}%{_bindir}/dotnet
for f in corerun coreconsole crossgen ilasm ildasm; do cp %{deliverydir}/$f %{buildroot}%{_bindir}/dotnet; done
mkdir -p %{buildroot}%{_libdir}
cp %{deliverydir}/*.so %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cp %{deliverydir}/inc/*.h %{buildroot}%{_includedir}
cp %{deliverydir}/*.dll %{buildroot}%{_libdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
# TODO license or copyright
%{_bindir}/dotnet/*
%{_libdir}/*.so
%{_libdir}/*.dll
%{_includedir}/*.h

%changelog
* Mon Nov 21 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.1.0-1
- upgrade to 1.1.0

* Thu Aug 18 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.0.4-1
- upgrade to 1.0.4

* Wed Jan 06 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.0.0-1
- initial package for .NET Core (from git master)
