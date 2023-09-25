
# Labelling Method Not Allowed Exception

## Structure

`LabellingMethodNotAllowedException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | [`str`](../../doc/models/string-enum.md) | Optional | - |
| `http_status_code` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "message": "Only POST requests allowed",
  "http_status_code": 405.0
}
```

