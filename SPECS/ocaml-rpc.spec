%global debug_package %{nil}

Name:           ocaml-rpc
Version:        1.9.2
Release:        1%{?dist}
Summary:        An RPC library for OCaml
License:        LGPL
URL:            https://github.com/jonludlam/ocaml-rpc
Source0:        https://github.com/jonludlam/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  oasis
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-type-conv
BuildRequires:  ocaml-xmlm-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppxtools-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-rresult-devel
BuildRequires:  ocaml-async-devel

%description
Am RPC library for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-camlp4-devel%{?_isa}
Requires:       ocaml-type-conv%{?_isa}
Requires:       ocaml-lwt%{?_isa}
Requires:       ocaml-xmlm-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}

%files
%doc README.md
%{_libdir}/ocaml/rpclib
%exclude %{_libdir}/ocaml/rpclib/*.cmx
%exclude %{_libdir}/ocaml/rpclib/*.cmxa
%exclude %{_libdir}/ocaml/rpclib/*.cmxs
%exclude %{_libdir}/ocaml/rpclib/*.annot
%exclude %{_libdir}/ocaml/rpclib/*.cmt
%exclude %{_libdir}/ocaml/rpclib/*.cmti
%{_libdir}/ocaml/ppx_deriving_rpc
%exclude %{_libdir}/ocaml/ppx_deriving_rpc/*.cmx
%exclude %{_libdir}/ocaml/ppx_deriving_rpc/*.cmxa
%exclude %{_libdir}/ocaml/ppx_deriving_rpc/*.cmxs
%exclude %{_libdir}/ocaml/ppx_deriving_rpc/*.annot
%exclude %{_libdir}/ocaml/ppx_deriving_rpc/*.cmt
%exclude %{_libdir}/ocaml/ppx_deriving_rpc/*.cmti


%files devel
%{_libdir}/ocaml/rpclib/*.cmx
%{_libdir}/ocaml/rpclib/*.cmxa
%{_libdir}/ocaml/rpclib/*.cmxs
%{_libdir}/ocaml/ppx_deriving_rpc/*.cmx
%{_libdir}/ocaml/ppx_deriving_rpc/*.cmxa
%{_libdir}/ocaml/ppx_deriving_rpc/*.cmxs

%changelog
* Tue Oct 25 2016 Marcello Seri <marcello.seri@citrix.com> - 1.9.2-1
- Update to 1.9.2

* Mon Sep 19 2016 Rob Hoes <rob.hoes@citrix.com> - 1.6.0-1
- Update to 1.6.0

* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 1.5.5-2
- Remove *.cmt, *.cmti and *.annot

* Thu Jul 23 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.5.5-1
- Update to 1.5.5

* Thu Jun 11 2015 John Else <john.else@citrix.com> - 1.5.4-1
- Update to 1.5.4, fixing upgrade of records with option type fields

* Tue Nov  4 2014 David Scott <dave.scott@citrix.com> - 1.5.3-1
- Update to 1.5.3, with support for upgrade

* Fri May 23 2014 Euan Harris <euan.harris@citrix.com> - 1.5.1-1
- Update to 1.5.1, removing dependency on js-of-ocaml

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.4.1-1
- Initial package

