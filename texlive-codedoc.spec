# revision 17630
# category Package
# catalog-ctan /macros/latex/contrib/codedoc
# catalog-date 2010-03-30 18:14:30 +0200
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-codedoc
Version:	0.3
Release:	1
Summary:	LaTeX code and documentation in LaTeX-format file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/codedoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codedoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codedoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The CodeDoc class is an alternative to DocStrip (and others) to
produce LaTeX code along with its documentation without
departing from LaTeX's ordinary syntax. The documentation is
prepared like any other LaTeX document and the code to be
commented verbatim is simply delimited by an environment. When
an option is turned on in the class options, this code is
written to the desired file(s). The class also includes fully
customizable verbatim environments which provide the author
with separate commands to typeset the material and/or to
execute it.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/codedoc/codedoc.cls
%doc %{_texmfdistdir}/doc/latex/codedoc/CodeDoc-manual.pdf
%doc %{_texmfdistdir}/doc/latex/codedoc/CodeDoc-manual.tex
%doc %{_texmfdistdir}/doc/latex/codedoc/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
