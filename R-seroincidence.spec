#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-seroincidence
Version  : 2.0.0
Release  : 40
URL      : https://cran.r-project.org/src/contrib/seroincidence_2.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/seroincidence_2.0.0.tar.gz
Summary  : Estimating Infection Rates from Serological Data
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
population sample into an estimate of the frequency with which
  seroconversions (infections) occur in the sampled population.

%prep
%setup -q -c -n seroincidence
cd %{_builddir}/seroincidence

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641121292

%install
export SOURCE_DATE_EPOCH=1641121292
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seroincidence
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seroincidence
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library seroincidence
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc seroincidence || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/seroincidence/CITATION
/usr/lib64/R/library/seroincidence/DESCRIPTION
/usr/lib64/R/library/seroincidence/INDEX
/usr/lib64/R/library/seroincidence/Meta/Rd.rds
/usr/lib64/R/library/seroincidence/Meta/data.rds
/usr/lib64/R/library/seroincidence/Meta/features.rds
/usr/lib64/R/library/seroincidence/Meta/hsearch.rds
/usr/lib64/R/library/seroincidence/Meta/links.rds
/usr/lib64/R/library/seroincidence/Meta/nsInfo.rds
/usr/lib64/R/library/seroincidence/Meta/package.rds
/usr/lib64/R/library/seroincidence/Meta/vignette.rds
/usr/lib64/R/library/seroincidence/NAMESPACE
/usr/lib64/R/library/seroincidence/NEWS
/usr/lib64/R/library/seroincidence/R/seroincidence
/usr/lib64/R/library/seroincidence/R/seroincidence.rdb
/usr/lib64/R/library/seroincidence/R/seroincidence.rdx
/usr/lib64/R/library/seroincidence/data/Rdata.rdb
/usr/lib64/R/library/seroincidence/data/Rdata.rds
/usr/lib64/R/library/seroincidence/data/Rdata.rdx
/usr/lib64/R/library/seroincidence/data/datalist
/usr/lib64/R/library/seroincidence/doc/cover.Rmd
/usr/lib64/R/library/seroincidence/doc/cover.html
/usr/lib64/R/library/seroincidence/doc/index.html
/usr/lib64/R/library/seroincidence/doc/installation.Rmd
/usr/lib64/R/library/seroincidence/doc/installation.pdf
/usr/lib64/R/library/seroincidence/doc/methodology.Rmd
/usr/lib64/R/library/seroincidence/doc/methodology.pdf
/usr/lib64/R/library/seroincidence/doc/tutorial.Rmd
/usr/lib64/R/library/seroincidence/doc/tutorial.pdf
/usr/lib64/R/library/seroincidence/help/AnIndex
/usr/lib64/R/library/seroincidence/help/aliases.rds
/usr/lib64/R/library/seroincidence/help/paths.rds
/usr/lib64/R/library/seroincidence/help/seroincidence.rdb
/usr/lib64/R/library/seroincidence/help/seroincidence.rdx
/usr/lib64/R/library/seroincidence/html/00Index.html
/usr/lib64/R/library/seroincidence/html/R.css
