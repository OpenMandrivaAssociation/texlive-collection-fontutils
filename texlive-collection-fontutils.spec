# revision 24759
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-fontutils
Version:	20120223
Release:	1
Summary:	Graphics TeX and outline font utilities
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-fontutils.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-accfonts
Requires:	texlive-afm2pl
Requires:	texlive-dosepsbin
Requires:	texlive-epstopdf
Requires:	texlive-fontware
Requires:	texlive-lcdftypetools
Requires:	texlive-ps2pkm
Requires:	texlive-pstools
Requires:	psutils
Requires:	texlive-dvipsconfig
Requires:	texlive-fontinst
Requires:	texlive-fontools
Requires:	texlive-mf2pt1
Requires:	texlive-ttfutils

%description
Programs for conversion between font formats, testing fonts,
virtual fonts, .gf and .pk manipulation, mft, fontinst, etc.
Manipulating OpenType, TrueType, PostScript Type 1, and
PostScript and other images.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
