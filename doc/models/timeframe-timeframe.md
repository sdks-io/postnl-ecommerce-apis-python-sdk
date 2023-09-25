
# Timeframe Timeframe

## Structure

`TimeframeTimeframe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mfrom` | [`str`](../../doc/models/string-enum.md) | Optional | The start time of the expected delivery window |
| `options` | [`Options2`](../../doc/models/options-2.md) | Optional | The delivery option for which the timeframe is calculated. See [Delivery Options](#tag/Reference-codes/Delivery-options) for possible values. |
| `to` | [`str`](../../doc/models/string-enum.md) | Optional | The end time of the expected delivery window |
| `sustainability` | [`Sustainability4`](../../doc/models/sustainability-4.md) | Optional | Sustainability score |

## Example (as JSON)

```json
{
  "From": "12:30:00",
  "To": "14:30:00",
  "Options": {
    "string": "Morning"
  },
  "Sustainability": {
    "Code": "Code2",
    "Description": "Description4"
  }
}
```

