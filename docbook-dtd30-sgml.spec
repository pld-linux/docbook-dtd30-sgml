Summary:	SGML document type definition for DocBook 3.0
Summary(es):	OASIS DTD DocBook Group para documentaci�n t�cnica
Summary(pl):	DTD dla dokument�w DocBook 3.0
Summary(pt_BR):	DTD DocBook Davenport Group para documenta��o t�cnica
Summary(ru):	SGML DTD ��� ����������� ������������ � ������� DocBook 3.0
Summary(uk):	SGML DTD ��� ���Φ��ϧ ���������æ� � �����Ԧ DocBook 3.0
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
OASIS DTD DocBook para documentaci�n t�cnica.

%description -l pl
DocBook DTD jest zestawem definicji dokument�w przeznaczonych do
tworzenia dokumentacji programistycznej. Ten pakiet zawiera wersj� 3.0
DTD.

%description -l pt_BR
DTD DocBook Davenport Group para documenta��o t�cnica.

%description -l ru
DocBook - ��� SGML DTD (document type definition) � ���������
���������� ����� � ������� ����������� ������������ (������, �����,
man-��������) ���� ��������� �������� SGML-�����������, ���
����������� � ����������� OASIS. ��� ������ 3.0 ����� DTD.

%description -l uk
DocBook - �� SGML DTD (document type definition), �� ����դ ���������
��Ǧ� � ������� ���Φ��ϧ ���������æ� (����Ԧ, �����, man-���Ҧ���).
��� ��������� � SGML-��ͦ����, ���� ���������� � ������æ�ͦ OASIS. ��
���Ӧ� 3.0 ����� DTD.

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
