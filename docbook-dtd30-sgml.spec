Summary:	SGML document type definition for DocBook 3.0
Summary(pl):	DTD dla dokumentów DocBook 3.0
Name:		docbook-dtd30-sgml
Version:	1.0
Release:	16
License:	distributable
Group:		Applications/Text
Source0:	http://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
Source1:	%{name}-Makefile
Patch0:		%{name}-catalog.patch
URL:		http://www.oasis-open.org/docbook/
BuildRequires:	unzip
Requires(post,postun):	sgml-common >= 0.5
Requires:	sgml-common >= 0.5
Provides:	docbook-dtd-sgml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages). This
syntax is SGML-compliant and is developed by the OASIS consortium.
This is the version 3.0 of this DTD.

%description -l pl
DocBook DTD jest zestawem definicji dokumentów przeznaczonych do
tworzenia dokumentacji programistycznej. Ten pakiet zawiera wersjê 3.0
DTD.

%prep
%setup -q -c
chmod -R a+rX,g-w,o-w .
cp %{SOURCE1} Makefile
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- docbook-dtd30-sgml < 1.0-15
if ! grep -q /etc/sgml/sgml-docbook-3.0.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/docbook/sgml-dtd-3.0/catalog > /dev/null
fi

%post
if ! grep -q /etc/sgml/sgml-docbook-3.0.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/docbook/sgml-dtd-3.0/catalog > /dev/null
fi

%postun
if [ "$1" = "0" ] ; then
	/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/docbook/sgml-dtd-3.0/catalog > /dev/null
fi

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/sgml/docbook/sgml-dtd-3.0
