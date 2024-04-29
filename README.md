# Solutions Code Studio Templates

This repository contains Cookiecutter templates for building web apps with your chosen framework and Code Studio templates for quickly starting your Code Studio projects.

Please refer to the [documentation](https://developer.dataiku.com/latest/tutorials/webapps/code-studio/index.html) for detailed instructions.

## Cookiecutter Templates

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a command-line utility for swiftly creating projects. This repository provides Angular and Vue.js templates packaged for smooth integration with DSS Code Studio.

### Usage

Ensure you have the Cookiecutter installer in your Code Env, then execute the following command:

```bash
$ cookiecutter gh:dataiku/solutions-code-studio-templates
```

It will prompt you to select a template:

```java
[1/1] Select template
  1 - Vue (./templates/vue)
  2 - Angular (./templates/angular)
  Choose from [1/2] (1):
```

After selection, you'll be asked to enter specific project parameters:

```java
[1/6] Choose your (Angular / Vue) project name (Angular Project):
[2/6] Version (0.0.1):
[3/6] Choose your client server port (default 4200) (4200):
[4/6] Choose your Flask backend port (default 5000) (5000):
[5/6] DSS instance (default):
[6/6] DSS project ():
```

### Using Your Own Cookiecutter Templates

We provide a seamless way to integrate your own Cookiecutter templates into the existing ones.

#### Repository Architecture

Your repository architecture must mirror that of this repository, with a main `cookiecutter.json` file pointing to specific templates and a `templates/` directory containing all your Cookiecutter templates.

```scss
cookiecutter.json
templates/
|_ template1/
  |_ cookiecutter.json
```

#### Main Cookiecutter File

The `cookiecutter.json` file at the root of the repository must have a **template** array listing all your templates:

```json
{
    "template": [
        "My own template (./templates/my-own-template)"
    ]
}
```

#### Environment Variables Configuration

To use your own Cookiecutter templates from a public or private GitHub repository, you need to set two environment variables:
- `PRIVATE_TEMPLATE_ACCESS` set to 1 to allow access to another repository.
- `PRIVATE_TEMPLATE_REPOSITORY` set with the SSH GitHub URL. For example, `git@github.com:cookiecutter/cookiecutter.git`.

#### Running

When running the following command:

```bash
$ cookiecutter gh:dataiku/solutions-code-studio-templates
```

It will include your private templates in the prompt:

```java
[1/1] Select template
  1 - Vue (./templates/vue)
  2 - Angular (./templates/angular)
  3 - My own template (./templates/my-own-template)
  Choose from [1/2/3] (1):
```

## Code Studio Templates

In the `code-studio` folder, we provide Code Studio Templates compatible with the latest DSS version as well as older versions.
