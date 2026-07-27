Name: qtxdg-tools
Version: 4.4.0
Release: 2
Source0: https://github.com/lxqt/qtxdg-tools/releases/download/%{version}/qtxdg-tools-%{version}.tar.xz
Summary: Tools for using xdg-utils with LXQt
URL: https://lxqt-project.org/
License: LGPL-2.1
Group: User Interface/Desktops
BuildSystem: cmake
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(qt6xdg) >= 3.9.1
BuildRequires: cmake(lxqt2-build-tools)

%patchlist
qtxdg-tools-qt-6.10.patch

%description
Tools for using xdg-utils with LXQt

%package devel
Summary: cmake files for locating qtxdg-tools
Group: User Interface/Desktops
Requires: %{name} = %{EVRD}

%description devel
cmake files for locating qtxdg-tools

%files
%{_bindir}/qtxdg-mat

%files devel
%{_datadir}/cmake/qtxdg-tools
