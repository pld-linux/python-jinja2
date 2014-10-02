#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	python2	# Python 2.x modules
%bcond_without	python3	# Python 3.x modules

%define		module	jinja2
Summary:	Jinja2 Template engine for Python 2.x
Summary(pl.UTF-8):	Silnik szablonów Jinja2 dla Pythona 2.x
Name:		python-%{module}
Version:	2.7.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
# Source0-md5:	b9dffd2f3b43d673802fe857c8445b1a
Patch0:		%{name}-docs.patch
URL:		http://jinja.pocoo.org/
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-markupsafe
Requires:	python-modules
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
Requires:	python3-modules

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
%patch0 -p1

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2
%endif
%if %{with python3}
%{__python3} setup.py build --build-base build-3
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/Jinja2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/Jinja2-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidoc
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
