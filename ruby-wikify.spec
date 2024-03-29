%define tarname wikify
Summary:	Wiki formatting library for Ruby
Summary(pl.UTF-8):	Biblioteka formatowania Wiki dla języka Ruby
Name:		ruby-wikify
Version:	1.0
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://community.nbtsc.org/~apollotiger/gadgets/%{tarname}-%{version}.tar.gz
# Source0-md5:	0716bc1168646715ecbbb4563a64e871
URL:		http://community.nbtsc.org/~apollotiger/ruby-wikify
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wikify.rb supplies String#wikify, allowing conversion from WikiMarkup
(e.g. "/foo -bar/ baz-") to proper XHTML 1.0 (e.g. "<em>foo
<strong>bar</strong></em><strong> baz</strong>").

%description -l pl.UTF-8
wikify.rb dostarcza String#wikify, umożliwiając konwersję z języka
WikiMarkup (np. "/foo -bar/ baz-") na odpowiedni kod XHTML 1.0 (np.
"<em>foo <strong>bar</strong></em><strong> baz</strong>").

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README
%{ruby_rubylibdir}/*
%{ruby_ridir}/String/wikify*
