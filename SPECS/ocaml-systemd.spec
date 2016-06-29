%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}
%global _use_internal_dependency_generator 0
%global __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%global __find_provides /usr/lib/rpm/ocaml-find-provides.sh

Name:           ocaml-systemd
Version:        1.1
Release:        1%{?dist}
Summary:        Ocaml Systemd bindings

License:        LGPL-3 with OCaml linking exception
URL:            https://github.com/juergenhoetzel/ocaml-systemd
Source0:        https://github.com/juergenhoetzel/ocaml-systemd/archive/%{version}/ocaml-systemd-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  chrpath
BuildRequires:  systemd-devel
BuildRequires:  oasis

%description
Ocaml systemd library bindings

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       systemd-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-systemd-%{version}

%build
oasis setup
make

%install
rm -rf $RPM_BUILD_ROOT
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

strip $OCAMLFIND_DESTDIR/stublibs/dll*.so
chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so

%files
%doc README.txt README.md
%dir %{_libdir}/ocaml/systemd/
%if %opt
%exclude %{_libdir}/ocaml/*/META
%exclude %{_libdir}/ocaml/*/*.annot
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%exclude %{_libdir}/ocaml/*/*.cma
%exclude %{_libdir}/ocaml/*/*.cmi
%exclude %{_libdir}/ocaml/*/*.cmt
%exclude %{_libdir}/ocaml/*/*.cmti
%exclude %{_libdir}/ocaml/*/*.cmxs
%endif
%exclude %{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%doc README.txt README.md
%if %opt
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.cmxs
%endif
%{_libdir}/ocaml/*/*.mli

%changelog
 * Wed Jun 29 2016 Rafal Mielniczuk <rafal.mielniczuk@eu.citrix.com> - 1.1-1
 - Initial package
