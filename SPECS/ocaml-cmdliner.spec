Name:           ocaml-cmdliner
Version:        0.9.8
Release:        1%{?dist}
Summary:        Declarative definition of commandline interfaces for OCaml
License:        BSD3
URL:            http://erratique.ch/software/cmdliner
Source0:        https://github.com/dbuenzli/cmdliner/archive/v%{version}/cmdliner-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
Obsoletes:      cmdliner <= 0.9.8

%description
Cmdliner is an OCaml module for the declarative definition of command line
interfaces. It provides a simple and compositional mechanism to convert
command line arguments to OCaml values and pass them to your functions.
The module automatically handles syntax errors, help messages and UNIX
man page generation. It supports programs with single or multiple commands
(like darcs or git) and respects most of the POSIX and GNU conventions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cmdliner-%{version}

%build
ocaml pkg/git.ml
ocaml pkg/build.ml native=true native-dynlink=true

%install
%__install -d  %{buildroot}/%{_libdir}/ocaml/cmdliner
%__install _build/src/cmdliner.a     %{buildroot}/%{_libdir}/ocaml/cmdliner
%__install _build/src/cmdliner.cma   %{buildroot}/%{_libdir}/ocaml/cmdliner
%__install _build/src/cmdliner.cmi   %{buildroot}/%{_libdir}/ocaml/cmdliner
%__install _build/src/cmdliner.cmx   %{buildroot}/%{_libdir}/ocaml/cmdliner
%__install _build/src/cmdliner.cmxa  %{buildroot}/%{_libdir}/ocaml/cmdliner
%__install _build/src/cmdliner.cmxs  %{buildroot}/%{_libdir}/ocaml/cmdliner
%__install _build/src/cmdliner.mli   %{buildroot}/%{_libdir}/ocaml/cmdliner
%__install _build/pkg/META           %{buildroot}/%{_libdir}/ocaml/cmdliner

%files
%doc CHANGES.md
%doc README.md
%{_libdir}/ocaml/cmdliner
%exclude %{_libdir}/ocaml/cmdliner/*.a
%exclude %{_libdir}/ocaml/cmdliner/*.cmxa
%exclude %{_libdir}/ocaml/cmdliner/*.cmx
%exclude %{_libdir}/ocaml/cmdliner/*.mli
%exclude %{_libdir}/ocaml/cmdliner/*.annot
%exclude %{_libdir}/ocaml/cmdliner/*.cmt
%exclude %{_libdir}/ocaml/cmdliner/*.cmti

%files devel
%{_libdir}/ocaml/cmdliner/*.a
%{_libdir}/ocaml/cmdliner/*.cmx
%{_libdir}/ocaml/cmdliner/*.cmxa
%{_libdir}/ocaml/cmdliner/*.mli

%changelog
* Tue Oct 25 2016 Christian Lindig <christian.lindig@citrix.com> - 0.9.8-1
- Update package version

* Mon Oct 24 2016 Christian Lindig <christian.lindig@citrix.com> - 0.9.5-4
- use install(1) rather than cp(1), mkdir(1) for installation; use RPM macros

* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 0.9.5-3
- Remove *.cmt, *.cmti and *.annot

* Tue Apr 7 2015 Euan Harris <euan.harris@citrix.com> - 0.9.5-2
- Switch back to GitHub mirror

* Thu Jul 17 2014 David Scott <dave.scott@citrix.com> - 0.9.5-1
- Update to 0.9.5

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-3
- Split files correctly between base and devel packages

* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Switch to GitHub mirror

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Initial package

