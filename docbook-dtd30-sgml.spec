Name: docbook-dtd30-sgml
Version: 1.0
Release: 10
Group: Applications/Text

Summary: SGML document type definition for DocBook.

License: Distributable
URL: http://www.oasis-open.org/docbook/

Provides: docbook-dtd-sgml
Requires: sgml-common >= 0.5
Requires(post,postun): sgml-common >= 0.5 fileutils

BuildRoot: %{_tmppath}/%{name}-%{version}

BuildArch: noarch
Source0: http://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
Source1: %{name}-%{version}.Makefile
Patch0: %{name}-%{version}.catalog.patch
BuildRequires: unzip

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This syntax is SGML-compliant and is developed by the OASIS consortium.
This is the version 3.0 of this DTD.


%prep
%setup -c -T
unzip %{SOURCE0}
if [ `id -u` -eq 0 ]; then
  chown -R root.root .
  chmod -R a+rX,g-w,o-w .
fi
cp %{SOURCE1} Makefile
patch -b docbook.cat $RPM_SOURCE_DIR/%{name}-%{version}.catalog.patch

%build


%install
DESTDIR=$RPM_BUILD_ROOT
rm -rf $DESTDIR
make install DESTDIR=$DESTDIR/usr/share/sgml/docbook/sgml-dtd-3.0


%clean
DESTDIR=$RPM_BUILD_ROOT
rm -rf $DESTDIR


%files
%defattr (-,root,root)
%doc *.txt
/usr/share/sgml/docbook/sgml-dtd-3.0


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
ln -s -f /etc/sgml/sgml-docbook-3.0.cat /etc/sgml/sgml-docbook.cat


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

%changelog
* Wed Jan 24 2001 Tim Waugh <twaugh@redhat.com>
- Scripts require fileutils.
- Make scripts quieter.

* Mon Jan 15 2001 Tim Waugh <twaugh@redhat.com>
- Don't play so many macro games.
- Don't use 'rpm' in post scripts.
- Make sure to own the sgml-dtd-3.0 directory.

* Sun Jan 14 2001 Tim Waugh <twaugh@redhat.com>
- Change requirement on /usr/bin/install-catalog to sgml-common.

* Fri Jan 12 2001 Tim Waugh <twaugh@redhat.com>
- Change Copyright: to License:.
- Remove Packager: line.

* Tue Jan 09 2001 Tim Waugh <twaugh@redhat.com>
- Change group.
- Use %%{_tmppath}.
- rm before install.
- openjade not jade.
- Correct typo.
- Build requires unzip.
- Require install-catalog for post and postun.

* Tue Jan 09 2001 Tim Waugh <twaugh@redhat.com>
- Based on Eric Bischoff's new-trials packages.
