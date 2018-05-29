#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	python2	# Python 2.x modules
%bcond_without	python3	# Python 3.x modules

%define		module	jinja2
Summary:	Jinja2 Template engine for Python 2.x
Summary(pl.UTF-8):	Silnik szablonów Jinja2 dla Pythona 2.x
Name:		python-%{module}
Version:	2.10
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/Jinja2
Source0:	https://files.pythonhosted.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
# Source0-md5:	61ef1117f945486472850819b8d1eb3d
URL:		http://jinja.pocoo.org/
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-markupsafe
Requires:	python-modules >= 1:2.6
Obsoletes:	python-Jinja2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small but fast and easy to use stand-alone template engine written
in pure Python. Provides a Django inspired non-XML syntax but supports
inline expressions and an optional sandboxed environment.

%description -l pl.UTF-8
Mały ale szybki i łatwy w użyciu samodzielny silnik szablonów napisany
w czystym Pythonie. Udostępnia podobne do Django, o odmiennej od XML-a
składni i kompilowane do kodu Pythona szablony w opcjonalnie
ograniczonym środowisku.

%package -n python3-%{module}
Summary:	Template engine Jinja2 for Python 3.x
Summary(pl.UTF-8):	Silnik szablonów Jinja2 dla Pythona 3.x
Group:		Development/Languages/Python
Requires:	python3-markupsafe
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
A small but fast and easy to use stand-alone template engine written
in pure Python. Provides a Django inspired non-XML syntax but supports
inline expressions and an optional sandboxed environment.

%description -n python3-%{module} -l pl.UTF-8
Mały ale szybki i łatwy w użyciu samodzielny silnik szablonów napisany
w czystym Pythonie. Udostępnia podobne do Django, o odmiennej od XML-a
składni i kompilowane do kodu Pythona szablony w opcjonalnie
ograniczonym środowisku.

%package apidoc
Summary:	Jinja2 template engine API documentation
Summary(pl.UTF-8):	Dokumentacja API silnika szablonów Jinja2
Group:		Development/Languages/Python

%description apidoc
API documentation for Jinja2 template engine.

%description apidoc -l pl.UTF-8
Dokumentacja API silnika szablonów Jinja2.

%prep
%setup -q -n Jinja2-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs -j1 html \
	SPHINXBUILD=sphinx-build
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
%doc AUTHORS CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/Jinja2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/Jinja2-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidoc
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
