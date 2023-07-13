# LLM Workflow Engine (LWE) AI21 Provider plugin

AI21 Provider plugin for [LLM Workflow Engine](https://github.com/llm-workflow-engine/llm-workflow-engine)

Access to [AI21](https://docs.ai21.com/docs/jurassic-2-models) models.

## Installation

### Export API key

Grab an AI21 API key from [https://studio.ai21.com/account/api-key](https://studio.ai21.com/account/api-key)

Export the key into your local environment:

```bash
export AI21_API_KEY=<API_KEY>
```

### From packages

Install the latest version of this software directly from github with pip:

```bash
pip install git+https://github.com/llm-workflow-engine/lwe-plugin-provider-ai21
```

### From source (recommended for development)

Install the latest version of this software directly from git:

```bash
git clone https://github.com/llm-workflow-engine/lwe-plugin-provider-ai21.git
```

Install the development package:

```bash
cd llm-workflow-engine
pip install -e .
```

## Configuration

Add the following to `config.yaml` in your profile:

```yaml
plugins:
  enabled:
    - provider_ai21
    # Any other plugins you want enabled...
```

## Usage

From a running LWE shell:

```
/provider ai21
/model model j2-large
```
