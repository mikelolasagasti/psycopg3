Name:           python-proxy
Version:        2.7.8
Release:        1%{?dist}
Summary:        Asynchronous tunnel proxy implemented in Python3 asyncio

License:        LGPLv3
URL:            https://github.com/qwj/python-proxy
Source0:        %{url}/archive/%{version}/python-proxy-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For check
BuildRequires:  pytest


%description
HTTP/HTTP2/HTTP3/Socks4/Socks5/Shadowsocks/SSH/Redirect/Pf/QUIC TCP/UDP
asynchronous tunnel proxy implemented in Python3 asyncio.

%package -n     python3-%{name}
Summary:        %{summary}

%description -n python3-%{name}
HTTP/HTTP2/HTTP3/Socks4/Socks5/Shadowsocks/SSH/Redirect/Pf/QUIC TCP/UDP
asynchronous tunnel proxy implemented in Python3 asyncio.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pproxy

# tests are custom

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/pproxy

%changelog
* Sat Nov 06 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.7.8-1
- Initial package
