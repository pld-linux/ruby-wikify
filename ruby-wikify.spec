%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"])')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Object-Relational mapping library for Ruby
Name:		ruby-wikify
%define tarname wikify
Version:	1.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://community.nbtsc.org/~apollotiger/gadgets/%{tarname}-%{version}.tar.gz
# Source0-md5:	1231f8cbf59d7464e0d17021822d91b7
uRL:		http://community.nbtsc.org/~apollotiger/ruby-wikify
BuildRequires:	ruby
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wikify.rb supplies String#wikify, allowing conversion from WikiMarkup
(e.g. "/foo -bar/ baz-") to proper XHTML 1.0 (e.g. "<em>foo
<strong>bar</strong></em><strong> baz</strong>").

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/String/wikify*
