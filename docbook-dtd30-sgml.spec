Summary:	SGML document type definition for DocBook 3.0
Summary(es.UTF-8):	OASIS DTD DocBook Group para documentación técnica
Summary(pl.UTF-8):	DTD dla dokumentów DocBook 3.0
Summary(pt_BR.UTF-8):	DTD DocBook Davenport Group para documentação técnica
Summary(ru.UTF-8):	SGML DTD для технической документации в формате DocBook 3.0
Summary(uk.UTF-8):	SGML DTD для технічної документації в форматі DocBook 3.0
Name:		docbook-dtd30-sgml
Version:	1.0
Release:	19
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

%description -l pl.UTF-8
DocBook DTD jest zestawem definicji dokumentów przeznaczonych do
tworzenia dokumentacji programistycznej. Ten pakiet zawiera wersję 3.0
DTD.

%description -l pt_BR.UTF-8
DTD DocBook Davenport Group para documentação técnica.

%description -l ru.UTF-8
DocBook - это SGML DTD (document type definition) с описанием
синтаксиса тегов в текстах технической документации (статьи, книги,
man-страницы) Этот синтаксис является SGML-совместимым, его
разработали в консорциуме OASIS. Это версия 3.0 этого DTD.

%description -l uk.UTF-8
DocBook - це SGML DTD (document type definition), що описує синтаксис
тегів в текстах технічної документації (статті, книги, man-сторінки).
Цей синтаксис є SGML-сумісним, його розроблено в консорціумі OASIS. Це
версія 3.0 цього DTD.

%prep
%setup -q -c
chmod -R a+rX,g-w,o-w .
cp %{SOURCE1} Makefile
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
