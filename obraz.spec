%global debug_package %{nil}

Name:           obraz
Version:        0.9.1
Release:        4%{?dist}
Summary:        Static site generator (fork)

License:        MIT
URL:            https://github.com/Bob131/obraz
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-PyYAML
BuildRequires:  python3-jinja2
BuildRequires:  python3-markdown
BuildRequires:  python3-docopt

Requires:  python3-PyYAML
Requires:  python3-jinja2
Requires:  python3-markdown
Requires:  python3-docopt

%description

Static site generator in a single Python file mostly compatible with Jekyll.
This package is a fork of Obraz proper (http://obraz.pirx.ru) containing
some small fixes, as it has been unmaintained for some time.


%prep
%setup -q


%build
%py3_build


%install
%py3_install


#%check
#%{__python3} setup.py test


%files
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/obraz
%{_datadir}/obraz/*
