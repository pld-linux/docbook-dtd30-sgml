Summary:	SGML document type definition for DocBook 3.0
Summary(es):	OASIS DTD DocBook Group para documentaciСn tИcnica
Summary(pl):	DTD dla dokumentСw DocBook 3.0
Summary(pt_BR):	DTD DocBook Davenport Group para documentaГЦo tИcnica
Summary(ru):	SGML DTD для технической документации в формате DocBook 3.0
Summary(uk):	SGML DTD для техн╕чно╖ документац╕╖ в формат╕ DocBook 3.0
Name:		docbook-dtd30-sgml
Version:	1.0
Release:	17
License:	distributable
Group:		Applications/Text
Source0:	http://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
# Source0-md5:	9a7f5b1b7dd52d0ca4fb080619f0459c
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

%description -l es
OASIS DTD DocBook para documentaciСn tИcnica.

%description -l pl
DocBook DTD jest zestawem definicji dokumentСw przeznaczonych do
tworzenia dokumentacji programistycznej. Ten pakiet zawiera wersjЙ 3.0
DTD.

%description -l pt_BR
DTD DocBook Davenport Group para documentaГЦo tИcnica.

%description -l ru
DocBook - это SGML DTD (document type definition) с описанием
синтаксиса тегов в текстах технической документации (статьи, книги,
man-страницы) Этот синтаксис является SGML-совместимым, его
разработали в консорциуме OASIS. Это версия 3.0 этого DTD.

%description -l uk
DocBook - це SGML DTD (document type definition), що опису╓ синтаксис
тег╕в в текстах техн╕чно╖ документац╕╖ (статт╕, книги, man-стор╕нки).
Цей синтаксис ╓ SGML-сум╕сним, його розроблено в консорц╕ум╕ OASIS. Це
верс╕я 3.0 цього DTD.

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
