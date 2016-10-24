%global debug_package %{nil}

Name:           ocaml-rresult
Version:        0.5.0
Release:        1%{?dist}
Summary:        Result value combinators for OCaml
License:        ISC
URL:            https://github.com/dbuenzli/rresult
Source0:        https://github.com/dbuenzli/rresult/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-topkg-devel

%description
Rresult is an OCaml module for handling computation results and errors
in an explicit and declarative manner without resorting to exceptions.
It defines combinators to operate on the values of the result type available
from OCaml 4.03 in the standard library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n rresult-%{version}

%build
ocaml pkg/pkg.ml build

%install
%__install -D _build/pkg/META                     %{buildroot}/%{_libdir}/ocaml/rresult/META
%__install -D _build/src/rresult.a                %{buildroot}/%{_libdir}/ocaml/rresult/rresult.a
%__install -D _build/src/rresult.cma              %{buildroot}/%{_libdir}/ocaml/rresult/rresult.cma
%__install -D _build/src/rresult.cmi              %{buildroot}/%{_libdir}/ocaml/rresult/rresult.cmi
%__install -D _build/src/rresult.cmti             %{buildroot}/%{_libdir}/ocaml/rresult/rresult.cmti
%__install -D _build/src/rresult.cmx              %{buildroot}/%{_libdir}/ocaml/rresult/rresult.cmx
%__install -D _build/src/rresult.cmxa             %{buildroot}/%{_libdir}/ocaml/rresult/rresult.cmxa
%__install -D _build/src/rresult.cmxs             %{buildroot}/%{_libdir}/ocaml/rresult/rresult.cmxs
%__install -D _build/src/rresult.mli              %{buildroot}/%{_libdir}/ocaml/rresult/rresult.mli
%__install -D _build/src/rresult_top.a            %{buildroot}/%{_libdir}/ocaml/rresult/rresult_top.a
%__install -D _build/src/rresult_top.cma          %{buildroot}/%{_libdir}/ocaml/rresult/rresult_top.cma
%__install -D _build/src/rresult_top.cmx          %{buildroot}/%{_libdir}/ocaml/rresult/rresult_top.cmx
%__install -D _build/src/rresult_top.cmxa         %{buildroot}/%{_libdir}/ocaml/rresult/rresult_top.cmxa
%__install -D _build/src/rresult_top.cmxs         %{buildroot}/%{_libdir}/ocaml/rresult/rresult_top.cmxs
%__install -D _build/src/rresult_top_init.ml      %{buildroot}/%{_libdir}/ocaml/rresult/rresult_top_init.ml


%files
%doc CHANGES.md
%doc LICENSE.md
%doc README.md
%{_libdir}/ocaml/rresult
%exclude %{_libdir}/ocaml/rresult/*.a
%exclude %{_libdir}/ocaml/rresult/*.mli
%exclude %{_libdir}/ocaml/rresult/*.cmti
%exclude %{_libdir}/ocaml/rresult/*.cmx
%exclude %{_libdir}/ocaml/rresult/*.cmxa
%exclude %{_libdir}/ocaml/rresult/*.cmxs

%files devel
%{_libdir}/ocaml/rresult/*.a
%{_libdir}/ocaml/rresult/*.mli
%{_libdir}/ocaml/rresult/*.cmx
%{_libdir}/ocaml/rresult/*.cmxa
%{_libdir}/ocaml/rresult/*.cmxs

%changelog
* Thu Oct 24 2016 Marcello Seri <marcello.seri@citrix.com> - 0.5.0-1
- Initial packaging.
