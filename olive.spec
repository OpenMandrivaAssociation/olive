%define unstable master
%define date 2021.09.01


Name:           olive
Version:        0.%{date}
Release:        1
Summary:        Olive is a free non-linear video editor for Windows, macOS, and Linux.
License:        GPL3
Group:          Video
URL:            https://www.olivevideoeditor.org/
#Source0:        https://github.com/olive-editor/olive/archive/continuous/olive-continuous.tar.gz
Source0:        https://github.com/olive-editor/olive/archive/refs/heads/olive-master.tar.gz

BuildRequires:  qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  qmake5
BuildRequires:  rpm-helper
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(frei0r)
BuildRequires:  pkgconfig(OpenColorIO)
BuildRequires:  cmake(OpenImageIO)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(Imath)

%description
Olive is a free non-linear video editor for Windows, macOS, and Linux.

%prep
%setup -q -n %{name}-%{unstable}

%build
%cmake
%make_build

%install
%make_install -C build


%files
%{_bindir}/%{name}-editor
%{_datadir}/applications/org.olivevideoeditor.Olive.desktop
%{_iconsdir}/hicolor/*/apps/org.olivevideoeditor.Olive.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-vnd.olive-project.png
%{_datadir}/metainfo/org.olivevideoeditor.Olive.appdata.xml
%{_datadir}/mime/packages/org.olivevideoeditor.Olive.xml
%{_datadir}/olive-editor/effects/*
