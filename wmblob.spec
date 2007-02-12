Summary:	wmblob is a useless program which shows moving blobs
Summary(pl.UTF-8):   wmblob jest bezużytecznym programem, który pokazuje ruchome kleksy
Name:		wmblob
Version:	1.0.1
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dockapps.org/files/155/440/%{name}-%{version}.tar.bz2
# Source0-md5:	b72497b8e61e1b0e5cfabd050d62fb11
Source1:	%{name}.desktop
URL:		http://dockapps.org/file.php/id/155
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmblob is a useless program which shows moving blobs. It is a nice
dockapp for Window Maker and it may run with other window mangers.

%description -l pl.UTF-8
wmblob jest bezużytecznym programem, który pokazuje ruchome kleksy.
Bardzo miła dokowalna aplikacja dla Window Makera i nie tylko.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/docklets/wmblob.desktop
