#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension imagesvg
Summary(pl.UTF-8):	Rozszerzenie Sphinksa imagesvg
Name:		python-sphinxcontrib-imagesvg
Version:	0.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-imagesvg/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-imagesvg/sphinxcontrib-imagesvg-%{version}.tar.gz
# Source0-md5:	e729caf9029627a231f6953fddd8c7d2
URL:		https://pypi.org/project/sphinxcontrib-imagesvg/
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules
Requires:	python-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the imagesvg Sphinx extension. The extension
defines a directive, "imagesvg", for embedding an SVG image in a
specified HTML tag.

%description -l pl.UTF-8
Ten pakiet zawiera rozszerzenie Sphinksa imagesvg. Definiuje ono
dyrektywę "imagesvg" do osadzania obrazów SVG w podanym znaczniku
HTML.

%package -n python3-sphinxcontrib-imagesvg
Summary:	Sphinx extension imagesvg
Summary(pl.UTF-8):	Rozszerzenie Sphinksa imagesvg
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-sphinxcontrib

%description -n python3-sphinxcontrib-imagesvg
This package contains the imagesvg Sphinx extension. The extension
defines a directive, "imagesvg", for embedding an SVG image in a
specified HTML tag.

%description -n python3-sphinxcontrib-imagesvg -l pl.UTF-8
Ten pakiet zawiera rozszerzenie Sphinksa imagesvg. Definiuje ono
dyrektywę "imagesvg" do osadzania obrazów SVG w podanym znaczniku
HTML.

%prep
%setup -q -n sphinxcontrib-imagesvg-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/sphinxcontrib/imagesvg.py[co]
%{py_sitescriptdir}/sphinxcontrib_imagesvg-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_imagesvg-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-imagesvg
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/imagesvg.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/imagesvg.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_imagesvg-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_imagesvg-%{version}-py*-nspkg.pth
%endif
