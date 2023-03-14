%define unstable continuous
%define date 12.01.2022


Name:           olive
Version:        0.2022.01.15
Release:        4
Summary:        Olive is a free non-linear video editor for Windows, macOS, and Linux.
License:        GPL3
Group:          Video
URL:            https://www.olivevideoeditor.org/
#Source0:        https://github.com/olive-editor/olive/archive/continuous/olive-continuous.tar.gz
Source0:        %{name}-%{unstable}-%{version}.tar.xz
Patch0:		olive-2022.01.15-ffmpeg-5.0.patch

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
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(frei0r)
BuildRequires:  pkgconfig(OpenColorIO)
BuildRequires:	pkgconfig(OpenImageIO)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(libglvnd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	cmake ninja

%description
Olive is a free non-linear video editor for Windows, macOS, and Linux.

%prep
%autosetup -p1 -n %{name}-%{unstable}-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/%{name}-editor
%{_datadir}/applications/org.olivevideoeditor.Olive.desktop
%{_iconsdir}/hicolor/*/apps/org.olivevideoeditor.Olive.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-vnd.olive-project.png
%{_datadir}/metainfo/org.olivevideoeditor.Olive.appdata.xml
%{_datadir}/mime/packages/org.olivevideoeditor.Olive.xml
