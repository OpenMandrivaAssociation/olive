%define snap 20181223

Name:           olive
Version:        0.%{snap}
Release:        1
Summary:        Olive is a free non-linear video editor for Windows, macOS, and Linux.
License:        GPL3
Group:          Video
URL:            https://www.olivevideoeditor.org/
Source0:        https://github.com/olive-editor/%{name}/archive/%{snap}/%{name}-%{snap}.tar.gz
BuildRequires:  qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  qmake5
BuildRequires:  rpm-helper
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  ffmpeg-devel

%description
Olive is a free non-linear video editor for Windows, macOS, and Linux.

%prep
%setup -q -n %{name}-%{snap}

%build
qmake olive.pro

%make_build

%install

%make_install

%files
%{_bindir}/*
