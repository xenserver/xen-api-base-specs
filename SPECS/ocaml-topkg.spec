%global debug_package %{nil}

Name:           ocaml-topkg
Version:        0.7.8
Release:        1%{?dist}
Summary:        The transitory OCaml software packager
License:        ISC
URL:            https://github.com/dbuenzli/topkg
Source0:        https://github.com/dbuenzli/topkg/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-result-devel

%description
Topkg is a packager for distributing OCaml software. It provides an API to
describe the files a package installs in a given build configuration and to
specify information about the package's distribution creation and publication
procedures. The optional topkg-care package is not included.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n topkg-%{version}

%build
ocaml pkg/pkg.ml build

%install
%__install -D _build/pkg/META                     %{buildroot}/%{_libdir}/ocaml/topkg/META
%__install -D _build/src/topkg.a                  %{buildroot}/%{_libdir}/ocaml/topkg/topkg.a
%__install -D _build/src/topkg.cma                %{buildroot}/%{_libdir}/ocaml/topkg/topkg.cma
%__install -D _build/src/topkg.cmi                %{buildroot}/%{_libdir}/ocaml/topkg/topkg.cmi
%__install -D _build/src/topkg.cmti               %{buildroot}/%{_libdir}/ocaml/topkg/topkg.cmti
%__install -D _build/src/topkg.cmx                %{buildroot}/%{_libdir}/ocaml/topkg/topkg.cmx
%__install -D _build/src/topkg.cmxa               %{buildroot}/%{_libdir}/ocaml/topkg/topkg.cmxa
%__install -D _build/src/topkg.cmxs               %{buildroot}/%{_libdir}/ocaml/topkg/topkg.cmxs
%__install -D _build/src/topkg.mli                %{buildroot}/%{_libdir}/ocaml/topkg/topkg.mli
%__install -D _build/src/topkg_build.cmx          %{buildroot}/%{_libdir}/ocaml/topkg/topkg_build.cmx
%__install -D _build/src/topkg_cmd.cmx            %{buildroot}/%{_libdir}/ocaml/topkg/topkg_cmd.cmx
%__install -D _build/src/topkg_codec.cmx          %{buildroot}/%{_libdir}/ocaml/topkg/topkg_codec.cmx
%__install -D _build/src/topkg_conf.cmx           %{buildroot}/%{_libdir}/ocaml/topkg/topkg_conf.cmx
%__install -D _build/src/topkg_distrib.cmx        %{buildroot}/%{_libdir}/ocaml/topkg/topkg_distrib.cmx
%__install -D _build/src/topkg_fexts.cmx          %{buildroot}/%{_libdir}/ocaml/topkg/topkg_fexts.cmx
%__install -D _build/src/topkg_fpath.cmx          %{buildroot}/%{_libdir}/ocaml/topkg/topkg_fpath.cmx
%__install -D _build/src/topkg_install.cmx        %{buildroot}/%{_libdir}/ocaml/topkg/topkg_install.cmx
%__install -D _build/src/topkg_ipc.cmx            %{buildroot}/%{_libdir}/ocaml/topkg/topkg_ipc.cmx
%__install -D _build/src/topkg_log.cmx            %{buildroot}/%{_libdir}/ocaml/topkg/topkg_log.cmx
%__install -D _build/src/topkg_main.cmx           %{buildroot}/%{_libdir}/ocaml/topkg/topkg_main.cmx
%__install -D _build/src/topkg_opam.cmx           %{buildroot}/%{_libdir}/ocaml/topkg/topkg_opam.cmx
%__install -D _build/src/topkg_os.cmx             %{buildroot}/%{_libdir}/ocaml/topkg/topkg_os.cmx
%__install -D _build/src/topkg_pkg.cmx            %{buildroot}/%{_libdir}/ocaml/topkg/topkg_pkg.cmx
%__install -D _build/src/topkg_publish.cmx        %{buildroot}/%{_libdir}/ocaml/topkg/topkg_publish.cmx
%__install -D _build/src/topkg_result.cmx         %{buildroot}/%{_libdir}/ocaml/topkg/topkg_result.cmx
%__install -D _build/src/topkg_string.cmx         %{buildroot}/%{_libdir}/ocaml/topkg/topkg_string.cmx
%__install -D _build/src/topkg_test.cmx           %{buildroot}/%{_libdir}/ocaml/topkg/topkg_test.cmx
%__install -D _build/src/topkg_vcs.cmx            %{buildroot}/%{_libdir}/ocaml/topkg/topkg_vcs.cmx


%files
%doc README.md
%doc LICENSE.md
%doc CHANGES.md
%{_libdir}/ocaml/topkg
%exclude %{_libdir}/ocaml/topkg/*.a
%exclude %{_libdir}/ocaml/topkg/*.mli
%exclude %{_libdir}/ocaml/topkg/*.cmti
%exclude %{_libdir}/ocaml/topkg/*.cmx
%exclude %{_libdir}/ocaml/topkg/*.cmxa
%exclude %{_libdir}/ocaml/topkg/*.cmxs

%files devel
%{_libdir}/ocaml/topkg/*.a
%{_libdir}/ocaml/topkg/*.mli
%{_libdir}/ocaml/topkg/*.cmx
%{_libdir}/ocaml/topkg/*.cmxa
%{_libdir}/ocaml/topkg/*.cmxs

%changelog
* Mon Oct 24 2016 Christian Lindig <christian.lindig@citrix.com> - 0.7.8-1
- Initial packaging.
