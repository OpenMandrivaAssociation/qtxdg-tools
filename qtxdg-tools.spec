Name: qtxdg-tools
Version: 3.10.0
Release: 2
Source0: https://github.com/lxqt/qtxdg-tools/releases/download/%{version}/qtxdg-tools-%{version}.tar.xz
Summary: Tools for using xdg-utils with LXQt
URL: https://lxqt-project.org/
License: LGPL-2.1
Group: User Interface/Desktops
BuildRequires: cmake(Qt5Core)
BuildRequires: qmake5
BuildRequires: cmake(qt5xdg) >= 3.9.1
BuildRequires: cmake(lxqt-build-tools)
BuildRequires: cmake ninja

%description
Tools for using xdg-utils with LXQt

%package devel
Summary: cmake files for locating qtxdg-tools
Group: User Interface/Desktops
Requires: %{name} = %{EVRD}

%description devel
cmake files for locating qtxdg-tools

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/qtxdg-mat

%files devel
%{_datadir}/cmake/qtxdg-tools
