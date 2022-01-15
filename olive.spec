%define unstable continuous
%define date 12.01.2022


Name:           olive
Version:        0.2022.01.15
Release:        1
Summary:        Olive is a free non-linear video editor for Windows, macOS, and Linux.
License:        GPL3
Group:          Video
URL:            https://www.olivevideoeditor.org/
#Source0:        https://github.com/olive-editor/olive/archive/continuous/olive-continuous.tar.gz
Source0:        %{name}-%{unstable}-%{version}.tar.xz

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
BuildRequires:	pkgconfig(OpenImageIO)
BuildRequires:	pkgconfig(portaudio-2.0)


%description
Olive is a free non-linear video editor for Windows, macOS, and Linux.

%prep
%setup -q -n %{name}-%{unstable}-%{version}

%build
%cmake

#%%qmake_qt5 PREFIX=/usr

%make_build

%install
mkdir -p %{buildroot}%{_bindir}
cd build
%make_install  INSTALL_ROOT=%{buildroot}


%files
%{_bindir}/%{name}-editor
%{_datadir}/applications/org.olivevideoeditor.Olive.desktop
%{_iconsdir}/hicolor/*/apps/org.olivevideoeditor.Olive.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-vnd.olive-project.png
%{_datadir}/metainfo/org.olivevideoeditor.Olive.appdata.xml
%{_datadir}/mime/packages/org.olivevideoeditor.Olive.xml
#%%{_datadir}/olive-editor/effects/*
