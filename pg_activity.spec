%global module_name pgactivity

Name:           pg_activity
Version:        2.2.1
Release:        1%{?dist}
Summary:        Command line tool for PostgreSQL server activity monitoring

License:        PostgreSQL
URL:            https://github.com/dalibo/pg_activity/
Source0:        https://github.com/dalibo/pg_activity/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# for check
BuildRequires:  pytest
BuildRequires:  python3dist(pytest-postgresql)
BuildRequires:  python3dist(psycopg2)
BuildRequires:  python3dist(psycopg)
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server

Requires:       python3dist(psycopg2)

%description
Top like application for PostgreSQL server activity monitoring

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires -r -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module_name}

%check
%pytest

%files -n %{name} -f %{pyproject_files}
%license LICENSE.txt
%doc AUTHORS.md README.md
%{_bindir}/pg_activity
%{_mandir}/man1/%{name}*

%changelog
* Thu Sep 02 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.2.1-1
- Version update to 2.2.1
- Adapt to pyproject-rpm-macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.5-2
- Rebuilt for Python 3.10

* Mon Apr 19 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.5-1
- Version update to 2.1.5

* Sat Apr 03 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.4-1
- Version update to 2.1.4

* Wed Mar 17 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.3-1
- Version update to 2.1.3

* Fri Mar 12 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.2-1
- Version update to 2.1.2
- Fix #1937228 FTBFS with Python-3.10

* Thu Mar 11 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.1-1
- Version update to 2.1.1

* Mon Mar 08 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.1.0-1
- Version update to 2.1.0
- Add check section

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.6.0-1
- Initial package.
- fix autosetup usage and license
