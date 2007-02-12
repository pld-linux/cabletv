Summary:	CableCrypt Decoder
Summary(pl.UTF-8):   Dekoder CableCrypt
Name:		cabletv
Version:	1.3.9
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://sector17.tvand.net/cabletv/download/%{name}-%{version}.tar.bz2
# Source0-md5:	ef099044034ecf1ba94769868f3c0a92
URL:		http://sector17.tvand.net/cabletv/
BuildRequires:	XFree86-devel
BuildRequires:	lirc-devel
BuildRequires:	sed >= 4.0
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CableCrypt Decoder.

%description -l pl.UTF-8
Dekoder CableCrypt.

%prep
%setup -q

%build
sed -i -e 's#install-data-local:#install-data-local-disabled:#g' Makefile.in
%configure \
	--enable-lirc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_examplesdir}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
