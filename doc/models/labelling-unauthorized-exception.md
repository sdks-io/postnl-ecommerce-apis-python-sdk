
# Labelling Unauthorized Exception

## Structure

`LabellingUnauthorizedException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | [`str`](../../doc/models/string-enum.md) | Optional | - |
| `http_status_code` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "message": "Failed to resolve API Key variable 'request.header.apikey'",
  "http_status_code": 401.0
}
```

