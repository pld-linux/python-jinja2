%bcond_without	doc
%bcond_without	python2
%bcond_without	python3
%define module jinja2
Summary:	Template engine
Summary(pl.UTF-8):	Silnik szablonów
Name:		python-%{module}
Version:	2.5.5
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
# Source0-md5:	83b20c1eeb31f49d8e6392efae91b7d5
URL:		http://jinja.pocoo.org/
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%pyrequires_eq	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%pyrequires_eq	python3-modules
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small but fast and easy to use stand-alone template engine written
in pure python. Provides a Django inspired non-XML syntax but supports
inline expressions and an optional sandboxed environment.

%description -l pl.UTF-8
Mały ale szybkie i łatwy w użyciu samodzielny silnik szablonów
napisany w czystym Pythonie. Dostarcza podobne do Django, o odmiennej
od XMLa składni i kompliowane do kodu Pythona szablony w opcjonalnie
ograniczonym środowisku.

%package -n python3-%{module}
Summary:	Template engine
Summary(pl.UTF-8):      Silnik szablonów
Group:          Development/Languages/Python

%description
A small but fast and easy to use stand-alone template engine written
in pure python. Provides a Django inspired non-XML syntax but supports
inline expressions and an optional sandboxed environment.

%description -n python3-%{module} -l pl.UTF-8
Mały ale szybkie i łatwy w użyciu samodzielny silnik szablonów
napisany w czystym Pythonie. Dostarcza podobne do Django, o odmiennej
od XMLa składni i kompliowane do kodu Pythona szablony w opcjonalnie
ograniczonym środowisku.

%package apidoc
Summary:	Jinja2 template engine API documentation
Group:          Development/Languages/Python

%description apidoc
API documentation for Jinja2 template engine

%prep
%setup -q -n Jinja2-%{version}

%build
%if %{with python2}
%{__python} setup.py build --build-base py2
%endif
%if %{with python3}
%{__python3} setup.py build --build-base py3
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
	build --build-base py2 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base py3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py3_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc PKG-INFO AUTHORS CHANGES
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*Jinja*.egg*
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc PKG-INFO AUTHORS CHANGES
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*Jinja*.egg*
%endif

%if %{with doc}
%files apidoc
%defattr(644,root,root,755)
%doc docs/_build/html
%endif
