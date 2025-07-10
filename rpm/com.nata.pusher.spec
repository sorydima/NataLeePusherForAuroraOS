Name:       com.nata.pusher
Summary:    Pusher
Version:    1.0.0
Release:    1
Group:      Qt/Qt
License:    BSD-3-Clause
URL:        https://pusher.natalee.pro/login
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(aurorawebview)
BuildRequires:  pkgconfig(auroraapp)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Network)

%description
Fully-featured web push notifications within minutes.

%prep
%autosetup

%build
%qmake5
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%defattr(644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Jul 10 2025 Dmitry Sorokin <dim15168250@yandex.ru>
- We are moving to new infra, nowadays partners with VK.
