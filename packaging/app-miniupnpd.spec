
Name: app-miniupnpd
Epoch: 1
Version: 0.9.0
Release: 2%{dist}
Summary: MiniUPnP
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-network

%description
MiniUPnP provides the firewall with UPnP functionality

%package core
Summary: MiniUPnP - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-network-core
Requires: miniupnpd

%description core
MiniUPnP provides the firewall with UPnP functionality

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/miniupnpd
cp -r * %{buildroot}/usr/clearos/apps/miniupnpd/

install -d -m 0755 %{buildroot}/var/clearos/miniupnpd
install -D -m 0644 packaging/miniupnpd.php %{buildroot}/var/clearos/base/daemon/miniupnpd.php

%post
logger -p local6.notice -t installer 'app-miniupnpd - installing'

%post core
logger -p local6.notice -t installer 'app-miniupnpd-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/miniupnpd/deploy/install ] && /usr/clearos/apps/miniupnpd/deploy/install
fi

[ -x /usr/clearos/apps/miniupnpd/deploy/upgrade ] && /usr/clearos/apps/miniupnpd/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-miniupnpd - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-miniupnpd-core - uninstalling'
    [ -x /usr/clearos/apps/miniupnpd/deploy/uninstall ] && /usr/clearos/apps/miniupnpd/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/miniupnpd/controllers
/usr/clearos/apps/miniupnpd/htdocs
#/usr/clearos/apps/miniupnpd/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/miniupnpd/packaging
#%exclude /usr/clearos/apps/miniupnpd/unify.json
%dir /usr/clearos/apps/miniupnpd
%dir /var/clearos/miniupnpd
/usr/clearos/apps/miniupnpd/deploy
/usr/clearos/apps/miniupnpd/language
#/usr/clearos/apps/miniupnpd/libraries
/var/clearos/base/daemon/miniupnpd.php
