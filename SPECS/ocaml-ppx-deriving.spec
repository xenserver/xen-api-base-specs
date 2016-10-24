%global debug_package %{nil}

Name:           ocaml-ppx-deriving
Version:        4.1
Release:        1%{?dist}
Summary:        Type-driven code generation for OCaml >=4.02
License:        MIT
URL:            https://github.com/whitequark/ppx_deriving
Source0:        https://github.com/whitequark/ppx_deriving/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  cppo
BuildRequires:  ocaml-ounit
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-ppx-tools

%description
deriving is a library simplifying type-driven code generation on OCaml
>=4.02.  deriving includes a set of useful plugins: show, eq, ord, enum,
iter, map, fold, make, yojson, protobuf.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_deriving-%{version}

%build
make

%install
%__install -D _build/pkg/META                     %{buildroot}/%{_libdir}/ocaml/ppx_deriving/META
%__install -D _build/src/ppx_deriving.a           %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving.a
%__install -D _build/src/ppx_deriving.cma         %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving.cma
%__install -D _build/src/ppx_deriving.cmi         %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving.cmi
%__install -D _build/src/ppx_deriving.cmti        %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving.cmti
%__install -D _build/src/ppx_deriving.cmx         %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving.cmx
%__install -D _build/src/ppx_deriving.cmxa        %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving.cmxa
%__install -D _build/src/ppx_deriving.cmxs        %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving.cmxs
%__install -D _build/src/ppx_deriving.mli         %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving.mli
%__install -D _build/src/ppx_deriving_main.a      %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_main.a
%__install -D _build/src/ppx_deriving_main.cma    %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_main.cma
%__install -D _build/src/ppx_deriving_main.cmxa   %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_main.cmxa
%__install -D _build/src/ppx_deriving_main.cmxs   %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_main.cmxs
%__install -D _build/src/ppx_deriving_runtime.a   %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_runtime.a
%__install -D _build/src/ppx_deriving_runtime.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_runtime.cma
%__install -D _build/src/ppx_deriving_runtime.cmi %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_runtime.cmi
%__install -D _build/src/ppx_deriving_runtime.cmti %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_runtime.cmti
%__install -D _build/src/ppx_deriving_runtime.cmx %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_runtime.cmx
%__install -D _build/src/ppx_deriving_runtime.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_runtime.cmxa
%__install -D _build/src/ppx_deriving_runtime.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_runtime.cmxs
%__install -D _build/src/ppx_deriving_runtime.mli %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_runtime.mli
%__install -D _build/src_plugins/ppx_deriving_create.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_create.a
%__install -D _build/src_plugins/ppx_deriving_create.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_create.cma
%__install -D _build/src_plugins/ppx_deriving_create.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_create.cmxa
%__install -D _build/src_plugins/ppx_deriving_create.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_create.cmxs
%__install -D _build/src_plugins/ppx_deriving_enum.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_enum.a
%__install -D _build/src_plugins/ppx_deriving_enum.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_enum.cma
%__install -D _build/src_plugins/ppx_deriving_enum.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_enum.cmxa
%__install -D _build/src_plugins/ppx_deriving_enum.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_enum.cmxs
%__install -D _build/src_plugins/ppx_deriving_eq.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_eq.a
%__install -D _build/src_plugins/ppx_deriving_eq.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_eq.cma
%__install -D _build/src_plugins/ppx_deriving_eq.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_eq.cmxa
%__install -D _build/src_plugins/ppx_deriving_eq.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_eq.cmxs
%__install -D _build/src_plugins/ppx_deriving_fold.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_fold.a
%__install -D _build/src_plugins/ppx_deriving_fold.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_fold.cma
%__install -D _build/src_plugins/ppx_deriving_fold.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_fold.cmxa
%__install -D _build/src_plugins/ppx_deriving_fold.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_fold.cmxs
%__install -D _build/src_plugins/ppx_deriving_iter.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_iter.a
%__install -D _build/src_plugins/ppx_deriving_iter.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_iter.cma
%__install -D _build/src_plugins/ppx_deriving_iter.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_iter.cmxa
%__install -D _build/src_plugins/ppx_deriving_iter.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_iter.cmxs
%__install -D _build/src_plugins/ppx_deriving_make.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_make.a
%__install -D _build/src_plugins/ppx_deriving_make.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_make.cma
%__install -D _build/src_plugins/ppx_deriving_make.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_make.cmxa
%__install -D _build/src_plugins/ppx_deriving_make.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_make.cmxs
%__install -D _build/src_plugins/ppx_deriving_map.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_map.a
%__install -D _build/src_plugins/ppx_deriving_map.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_map.cma
%__install -D _build/src_plugins/ppx_deriving_map.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_map.cmxa
%__install -D _build/src_plugins/ppx_deriving_map.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_map.cmxs
%__install -D _build/src_plugins/ppx_deriving_ord.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_ord.a
%__install -D _build/src_plugins/ppx_deriving_ord.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_ord.cma
%__install -D _build/src_plugins/ppx_deriving_ord.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_ord.cmxa
%__install -D _build/src_plugins/ppx_deriving_ord.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_ord.cmxs
%__install -D _build/src_plugins/ppx_deriving_show.a %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_show.a
%__install -D _build/src_plugins/ppx_deriving_show.cma %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_show.cma
%__install -D _build/src_plugins/ppx_deriving_show.cmxa %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_show.cmxa
%__install -D _build/src_plugins/ppx_deriving_show.cmxs %{buildroot}/%{_libdir}/ocaml/ppx_deriving/ppx_deriving_show.cmxs

%files
%doc CHANGELOG.md
%doc LICENSE.txt
%doc README.md
%{_libdir}/ocaml/ppx_deriving
%exclude %{_libdir}/ocaml/ppx_deriving/*.a
%exclude %{_libdir}/ocaml/ppx_deriving/*.annot
%exclude %{_libdir}/ocaml/ppx_deriving/*.cmt
%exclude %{_libdir}/ocaml/ppx_deriving/*.cmti
%exclude %{_libdir}/ocaml/ppx_deriving/*.cmx
%exclude %{_libdir}/ocaml/ppx_deriving/*.cmxa
%exclude %{_libdir}/ocaml/ppx_deriving/*.cmxs
%exclude %{_libdir}/ocaml/ppx_deriving/*.mli

%files devel
%{_libdir}/ocaml/ppx_deriving/*.a
%{_libdir}/ocaml/ppx_deriving/*.cmx
%{_libdir}/ocaml/ppx_deriving/*.cmxa
%{_libdir}/ocaml/ppx_deriving/*.cmxs
%{_libdir}/ocaml/ppx_deriving/*.mli

%changelog
* Mon Oct 24 2016 Christian Lindig <christian.lindig@citrix.com> - 4.1-1
- Initial packaging

