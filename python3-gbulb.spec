%define mod_name gbulb
%define debug_package %{nil}

# SUSE doesn't have python3_pkgversion macro
%if 0%{?suse_version} == 1500 && 0%{?is_opensuse}
%global python3_pkgversion 3
%endif

Name:           python-%{mod_name}
Version:        0.6.1
Release:        1%{?dist}
Url:            http://github.com/nathan-hoad/gbulb
Summary:        GLib event loop for asyncio (PEP 3156)
License:        Apache-2.0
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/92/cb/d2a0e4899cde5aa797e31d77a0a7422dcd188d880bb38d0e9d1b1196e5c6/%{mod_name}-%{version}.tar.gz
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}

%description
Gbulb is a python library that implements a PEP 3156 interface for the GLib
main event loop. It is designed to be used together with the tulip reference
implementation.

%package -n python%{python3_pkgversion}-gbulb
Summary:        GLib event loop for asyncio (PEP 3156)

%description -n python%{python3_pkgversion}-gbulb
Gbulb is a python library that implements a PEP 3156 interface for the GLib
main event loop. It is designed to be used together with the tulip reference
implementation.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-gbulb
%doc AUTHORS.rst README.md CHANGELOG.md examples 
%{python3_sitelib}/%{mod_name}*

%changelog
