# PymoAPI example: asynchronous API in Python using FastAPI, Odmantic and MongoDB. 

> An example of CRUD services (REST) developed in Python with FastAPI, Odmandic and MongoDB.

<!--
[![Tests](https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/actions/workflows/tests.yml/badge.svg)](https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/actions/workflows/tests.yml)
[![Build](https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/actions/workflows/build.yml/badge.svg)](https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/actions/workflows/build.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/2526932393edd4100563/maintainability)](https://codeclimate.com/github/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2526932393edd4100563/test_coverage)](https://codeclimate.com/github/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/test_coverage)
[![License](https://img.shields.io/github/license/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api.svg)](https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api.svg)](https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/graphs/contributors)
[![PyPI](https://img.shields.io/pypi/v/wipbox.svg)](https://pypi.org/project/wipbox/)
[![PyPI](https://img.shields.io/pypi/pyversions/wipbox.svg)](https://pypi.org/project/wipbox/)
[![codecov](https://codecov.io/gh/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/branch/devel/graph/badge.svg?token=IGALD1N09C)](https://codecov.io/gh/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api)
-->

## Table of Contents

* [Synopsis](#synopsis)
* [Usage](#usage)
  * [Start application](#usage-startapp)
  * [Check if app is running](#usage-checkapp)
  * [Stop application](#usage-startapp)
* [Installation](#installation)
* [Build](#build)
* [Tests](#tests)
* [Développement](#develop)
* [Compatibility](#compatibility)
* [Issues](#issues)
* [Contributing](#contributing)
* [Credits](#credits)
* [Resources](#resources)
* [History](#history)
* [License](#license)

## <a name="synopsis">Synopsis</a>

An example of CRUD services (REST) developed in Python with FastAPI, Odmandic and MongoDB.

## <a name="requirements">Requirements</a>

- [Docker Engine](https://docs.docker.com/engine/)
  - Application tested using [Docker v20.10.15](https://docs.docker.com/engine/release-notes/#201015)
- [Docker Compose](https://docs.docker.com/compose/)
  - Application tested using [Docker Compose 1.29.2](https://docs.docker.com/compose/release-notes/#1292)

## <a name="usage">Usage</a>

### <a name="usage-startapp">Start application</a>

```shell
docker-compose up -d --build
```
After a while, you should access to API server at: http://localhost:8000/

NB. 
- Optional `--build` parameter force docker-compose to rebuild image.
- Optional but useful `-d` parameter force docker-compose to run in background.

### <a name="usage-checkapp">Check if app is running</a>

```shell
docker-compose ps 
```

should return two running services:
- the [FastAPI]() application: `app`;
- the [MongoDB](mongodb.com/) instance: `db`.

You could too check if the containers are running just using the `docker` command:

```shell
docker ps
```

### <a name="usage-stopapp">Stop application</a>

```shell
docker-compose down
```

## <a name="installation">Installation</a>

### "Manual" installation

Clone the repository:

```shell
git clone https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api pymo
cd pymo
git checkout main # or any branch, tag or commit...
```

Install dependencies:

```shell
pip3 install -r requirements.txt
```

Optionally, install dependencies to run unit tests:

```shell
pip3 install -r requirements-test.txt
```

## <a name="build">Build</a>

```shell
#todo
```

## <a name="tests">Tests</a>

```shell
#todo
```

### Code coverage

```shell
#todo
```

## Develop

Please install dependencies from files:

- `requirements.txt`
- `requirements-dev.txt`

Then install the [pre-commit](https://pre-commit.com/) hook to forbidden pushing code if unit tests are not passing.

## <a name="issues"> Issues</a>

Feel free to [submit issues](https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api/issues) and enhancement requests.

## <a name="contributing">Contributing</a>

Please refer to project's style guidelines and guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

1. **Fork** the repo on GitHub
2. **Clone** the project to your own machine
3. **Commit** changes to your own branch
4. **Push** your work back up to your fork
5. Submit a **Pull request** so that we can review your changes

**NOTE**: Be sure to merge the latest from "upstream" before making a pull request!

## <a name="credits">Credits</a>

Thank you very much to this used or integrated open source developments:

- `#todo`

## <a name="resources">Resources</a>

Among others, to carry out this large and infinite project, we made use, among many others, of the following documentary resources.

Thank you to their authors for sharing their knowledge with our team.

- `#todo`

### Version management

- [Semver 2.0.0](https://semver.org/)

### Unit tests

- [Unit test log output with python](https://memotut.com/en/8a92970f0f6e5309e1df/)

### Code quality

- [Github Actions for Python Project](https://docs.codeclimate.com/docs/github-actions-test-coverage)
- Code formatting: [Black](https://github.com/psf/black)
- Documentation formatting: [PyDocStyle](http://www.pydocstyle.org/en/stable/usage.html) 
- [isort](https://github.com/PyCQA/isort)

### CI/CD

- [Making a Python package](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)
- [Using pre-commit git hooks to automate code checks](https://ericmjl.github.io/essays-on-data-science/terminal/pre-commits/)
- [PyTest With GitHub Actions](https://blog.dennisokeeffe.com/blog/2021-08-08-pytest-with-github-actions)
- [GitHub Action: Python Coverage Comment](https://github.com/marketplace/actions/python-coverage-comment)]

## <a name="history">History</a>

Please refer to [the changelog file](CHANGELOG.md).

## <a name="license">License</a>

>
> This file is a part of [demo-docker_python_mongo_api](https://github.com/cyu-lpdw/fr-cyu-lpdw-courses-nosql-demo-docker_python_mongo_api) project.
>
>
> (c) 2022, [Département des Sciences Informatiques, Université de Cergy](https://depinfo.u-cergy.fr/) (#cyu)[https://cyu.fr]
> 
> Creative Commons Legal Code
> 
> CC0 1.0 Universal
>
>    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
>    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
>    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
>    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
>    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
>    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
>    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
>    HEREUNDER.
> 
> Statement of Purpose
> 
> The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").
>
> Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.
>
> For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.
>
> 1. Copyright and Related Rights. A Work made available under CC0 may be
   protected by copyright and related or neighboring rights ("Copyright and
   Related Rights"). Copyright and Related Rights include, but are not
   limited to, the following:
>
> i. the right to reproduce, adapt, distribute, perform, display,
communicate, and translate a Work;
> ii. moral rights retained by the original author(s) and/or performer(s);
> iii. publicity and privacy rights pertaining to a person's image or
likeness depicted in a Work;
> iv. rights protecting against unfair competition in regards to a Work,
subject to the limitations in paragraph 4(a), below;
v. rights protecting the extraction, dissemination, use and reuse of data
in a Work;
> vi. database rights (such as those arising under Directive 96/9/EC of the
European Parliament and of the Council of 11 March 1996 on the legal
protection of databases, and under any national implementation
thereof, including any amended or successor version of such
directive); and
> vii. other similar, equivalent or corresponding rights throughout the
world based on applicable law or treaty, and any national
implementations thereof.
>
> 2. Waiver. To the greatest extent permitted by, but not in contravention
   of, applicable law, Affirmer hereby overtly, fully, permanently,
   irrevocably and unconditionally waives, abandons, and surrenders all of
   Affirmer's Copyright and Related Rights and associated claims and causes
   of action, whether now known or unknown (including existing as well as
   future claims and causes of action), in the Work (i) in all territories
   worldwide, (ii) for the maximum duration provided by applicable law or
   treaty (including future time extensions), (iii) in any current or future
   medium and for any number of copies, and (iv) for any purpose whatsoever,
   including without limitation commercial, advertising or promotional
   purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
   member of the public at large and to the detriment of Affirmer's heirs and
   successors, fully intending that such Waiver shall not be subject to
   revocation, rescission, cancellation, termination, or any other legal or
   equitable action to disrupt the quiet enjoyment of the Work by the public
   as contemplated by Affirmer's express Statement of Purpose.
>
> 3. Public License Fallback. Should any part of the Waiver for any reason
   be judged legally invalid or ineffective under applicable law, then the
   Waiver shall be preserved to the maximum extent permitted taking into
   account Affirmer's express Statement of Purpose. In addition, to the
   extent the Waiver is so judged Affirmer hereby grants to each affected
   person a royalty-free, non transferable, non sublicensable, non exclusive,
   irrevocable and unconditional license to exercise Affirmer's Copyright and
   Related Rights in the Work (i) in all territories worldwide, (ii) for the
   maximum duration provided by applicable law or treaty (including future
   time extensions), (iii) in any current or future medium and for any number
   of copies, and (iv) for any purpose whatsoever, including without
   limitation commercial, advertising or promotional purposes (the
   "License"). The License shall be deemed effective as of the date CC0 was
   applied by Affirmer to the Work. Should any part of the License for any
   reason be judged legally invalid or ineffective under applicable law, such
   partial invalidity or ineffectiveness shall not invalidate the remainder
   of the License, and in such case Affirmer hereby affirms that he or she
   will not (i) exercise any of his or her remaining Copyright and Related
   Rights in the Work or (ii) assert any associated claims and causes of
   action with respect to the Work, in either case contrary to Affirmer's
   express Statement of Purpose.
>
> 4. Limitations and Disclaimers.
>
> a. No trademark or patent rights held by Affirmer are waived, abandoned,
surrendered, licensed or otherwise affected by this document.
> b. Affirmer offers the Work as-is and makes no representations or
warranties of any kind concerning the Work, express, implied,
statutory or otherwise, including without limitation warranties of
title, merchantability, fitness for a particular purpose, non
infringement, or the absence of latent or other defects, accuracy, or
the present or absence of errors, whether or not discoverable, all to
the greatest extent permissible under applicable law.
> c. Affirmer disclaims responsibility for clearing rights of other persons
that may apply to the Work or any use thereof, including without
limitation any person's Copyright and Related Rights in the Work.
Further, Affirmer disclaims responsibility for obtaining any necessary
consents, permissions or other rights required for any use of the
Work.
> d. Affirmer understands and acknowledges that Creative Commons is not a
party to this document and has no duty or obligation with respect to
this CC0 or use of the Work.

