Name:    notify-osd
Summary: On-screen notification display agent, implementing the FDO notification specification
Version: 0.9.25
Release: %mkrel 1
License: GPLv3
Group:   System/Servers
URL:     https://launchpad.net/notify-osd
Source0: http://launchpad.net/notify-osd/0.9/%{version}/+download/%{name}-%{version}.tar.gz
Source1: dbus.service
BuildRequires: dbus-glib-devel
BuildRequires: gtk2-devel
BuildRequires: libGConf2-devel
BuildRequires: libnotify-devel
BuildRequires: libwnck-devel
BuildRequires: intltool
Provides:  virtual-notification-daemon
Conflicts: xfce4-notifyd
Conflicts: notification-daemon
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Canonical's on-screen notification display agent, implementing the
FreeDesktop.org notification specification with semi-transparent click-through
bubbles.

The Desktop Notifications framework provides a standard way of doing passive
pop-up notifications on the Linux desktop. These are designed to make the user
aware of something without interrupting their work flow with a dialog box that
they must close.

The notify-osd agent presents these notifications as ephemeral overlays, which
don't prevent the user from working. The agent queues notifications so that
screen layout is carefully managed, and handles updates. It also introduces the
idea of "appends", which allow notifications to grow over time, for example in
the case of instant messages from a particular user.

This agent is part of a broader set of tools that applications can use to draw
attention or seek a decision from the user. There is a guideline for effective
use of the framework for developers, which helps determine the right approach
for an application in different scenarios.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
sed 's,{libdir},%{_libdir},' %SOURCE1 >%{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service

%find_lang %{name}

%clean
rm -rf %{buildroot}


%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}
%{_datadir}/dbus-1/services/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons/hicolor/scalable/status/README
%{_datadir}/%{name}/icons/hicolor/scalable/status/notification-*.svg
