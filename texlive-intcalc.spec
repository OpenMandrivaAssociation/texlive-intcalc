Name:		texlive-intcalc
Version:	53168
Release:	2
Summary:	Expandable arithmetic operations with integers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/intcalc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intcalc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intcalc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/intcalc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides expandable arithmetic operations with
integers, using the e-TeX extension \numexpr if it is
available.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/intcalc
%{_texmfdistdir}/tex/generic/intcalc
%doc %{_texmfdistdir}/doc/latex/intcalc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
