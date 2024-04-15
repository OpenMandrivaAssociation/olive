%define branch master


Name:           olive
Version:        0.2024.01.10
Release:        2
Summary:        Olive is a free non-linear video editor for Windows, macOS, and Linux.
License:        GPL3
Group:          Video
URL:            https://www.olivevideoeditor.org/
Source0:        https://github.com/olive-editor/olive/archive/refs/heads/%{branch}.tar.gz#/%{name}-%{version}.tar.gz
# Keep the submodules at the versions shown at
# https://github.com/olive-editor/olive/tree/master/ext
Source1:	https://github.com/olive-editor/KDDockWidgets/archive/8d2d0a5764f8393cc148a2296d511276a8ffe559.tar.gz
Source2:	https://github.com/olive-editor/core/archive/277792824801495e868580ca86f6e7a1b53e4779.tar.gz
Patch0:		olive-20230312-static-helper.patch
Patch1:		core-ffmpeg7.patch
Patch2:		olive-ffmpeg7.patch

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
BuildRequires:  pkgconfig(Qt5X11Extras)
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
%setup -n %{name}-%{branch}
tar xf %{S:1}
tar xf %{S:2}
rmdir ext/KDDockWidgets ext/core
mv KDDockWidgets* ext/KDDockWidgets
mv core* ext/core
%autopatch -p1
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
