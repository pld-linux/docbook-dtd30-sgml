Summary:	SGML document type definition for DocBook 3.0
Name:		docbook-dtd30-sgml
Version:	1.0
Release:	11
License:	Distributable
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
Source1:	%{name}-Makefile
Patch0:		%{name}-catalog.patch
URL:		http://www.oasis-open.org/docbook/
BuildRequires:	unzip
Requires:	sgml-common >= 0.5
Requires(post):		sgml-common >= 0.5
Requires(postun):	sgml-common >= 0.5
Requires:	fileutils
BuildArch:	noarch
Provides:	docbook-dtd-sgml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages). This
syntax is SGML-compliant and is developed by the OASIS consortium.
This is the version 3.0 of this DTD.


%prep
%setup -q -c -T
unzip %{SOURCE0}
chmod -R a+rX,g-w,o-w .
cp %{SOURCE1} Makefile
patch -b docbook.cat $RPM_SOURCE_DIR/%{name}-catalog.patch

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf *.txt

%clean
rm -rf $DESTDIR

%files
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/sgml/docbook/sgml-dtd-3.0


%post
# Update the centralized catalog corresponding to this version of the DTD
/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog > /dev/null
/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/docbook/sgml-dtd-3.0/catalog > /dev/null

# The following lines are for the case in which the style sheets were
# installed after another DTD but before this DTD
STYLESHEETS=$(echo /usr/share/sgml/docbook/dsssl-stylesheets-*)
STYLESHEETS=${STYLESHEETS##*/dsssl-stylesheets-}
if [ "$STYLESHEETS" != "*" ]; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/openjade-1.3/catalog > /dev/null
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/docbook/dsssl-stylesheets-$STYLESHEETS/catalog > /dev/null
fi

# Update the link to the current version of the DTD
ln -sf /etc/sgml/sgml-docbook-3.0.cat /etc/sgml/sgml-docbook.cat

%postun
# Update the centralized catalog corresponding to this version of the DTD
/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog > /dev/null
/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/docbook/sgml-dtd-3.0/catalog > /dev/null

# The following lines are for the case in which the style sheets were
# not uninstalled because there is still another DTD
STYLESHEETS=$(echo /usr/share/sgml/docbook/dsssl-stylesheets-*)
STYLESHEETS=${STYLESHEETS##*/dsssl-stylesheets-}
if [ "$STYLESHEETS" != "*" ]; then
	/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/openjade-1.3/catalog > /dev/null
	/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-3.0.cat /usr/share/sgml/docbook/dsssl-stylesheets-$STYLESHEETS/catalog > /dev/null
fi

# Update the link to the current version of the DTD
if [ ! -e /etc/sgml/sgml-docbook-3.0.cat ]; then
	rm -f /etc/sgml/sgml-docbook.cat
	OTHERCAT=`ls /etc/sgml/sgml-docbook-?.?.cat 2> /dev/null | head --lines 1`
	if [ -n "$OTHERCAT" ]; then ln -s $OTHERCAT /etc/sgml/sgml-docbook.cat; fi
fi
