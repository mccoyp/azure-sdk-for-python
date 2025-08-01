

# Release History

## 1.1.0b5 (Unreleased)

### Bugs Fixed

- Fixed `update_agent` to execute with body as a keyword parameter.

### Features Added

- Support `tool_resources` for run async operations.

### Bugs Fixed

- `AgentsResponseFormatOption`, `MessageInputContent`, `MessageAttachmentToolDefinition`, `AgentsToolChoiceOption` are now public.
- Fixed issues where the `runs.create_and_process` API call did not correctly handle the `AzureAISearchTool`, `FileSearchTool`, and `CodeInterpreterTool` when specified in the toolset parameter.
  
## 1.1.0b4 (2025-07-11)

### Features Added

- Added support for MCP tool. For more information, see https://aka.ms/FoundryAgentMCPDoc.
- New tool_resources parameter added to runs.create method. This parameter represents overridden enabled tool resources that the agent should use to run
the thread. Default value is None.

### Bugs Fixed

- `_AgentsClientOperationsMixin` is now private.

### Sample updates

- Added a sample showing usage of MCP tool, [`sample_agents_mcp.py`](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-agents/samples/agents_tools/sample_agents_mcp.py).
- Added a sample showing auto function call for a synchronous client, [`sample_agents_auto_function_call.py`](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-agents/samples/agents_tools/sample_agents_auto_function_call.py)
- Added a sample showing auto function call for an asynchronous client, [`sample_agents_auto_function_call_async.py`](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-agents/samples/agents_async/sample_agents_auto_function_call_async.py).


## 1.1.0b3 (2025-06-30)

### Features Added

- Added support for Deep Research tool. For more information, see https://aka.ms/agents-deep-research.

### Bugs Fixed

- Fixed a tracing related bug that caused an error when process was ending if messages or run steps were listed and the resulting list was not iterated completely.

### Sample updates

- The file search samples were updated to demonstrate retrieving text associated with citations.
- Added samples for file search citation with streaming.
- Added samples showing usage of Deep Research tool (sync and async).

## 1.1.0b2 (2025-06-09)

### Bugs Fixed

- `asyncio.gather` is used to make function tool calls in parallel for `async` scenario.
- Adding instrumentation for create_thread_and_run.
- Fixed a tracing related bug that caused process_thread_run span to not appear when streaming is used without event handler.

### Sample updates

- Changed all samples to use `AIProjectClient` which is recommended to specify endpoint and credential.
- Added `sample_agents_stream_iteration_with_functions.py`

## 1.1.0b1 (2025-05-20)

### Features Added

- API version is changed to 2025-05-15-preview.
- Add FabricTool, SharepointTool, and BingCustomSearchTool classes along with samples.

### Bugs Fixed

- Adding instrumentation for create_thread_and_run

## 1.0.0 (2025-05-15)

### Features Added

- First stable release of Azure AI Agents client library.

## 1.0.0b3 (2025-05-14)

### Features Added

- Internal updates based on TypeSpec finalization.

## 1.0.0b2 (2025-05-13)

### Breaking Changes

- Rename `get_last_text_message_by_role` to `get_last_message_text_by_role`.

## 1.0.0b1 (2025-05-07)

### Breaking Changes

- enable_auto_function_calls supports positional arguments instead of keyword arguments.
- Please see the [agents migration guide](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/AGENTS_MIGRATION_GUIDE.md) on how to use `azure-ai-projects` with `azure-ai-agents` package.
  
### Features Added

- Initial version - splits off Azure AI Agents functionality from the Azure AI Projects SDK.
- Azure AI Search tool, Bing Grounding tool, and Bing Custom Search tool parameters updated.
- All polling functions now support timeout keyword parameter.

### Bugs Fixed

- During automatic function calls for streaming, when the thread run is cancelled due to too many retry, now a cancelled event will be sent out.
- Add missing thread run id and message id on the process thread run span.
