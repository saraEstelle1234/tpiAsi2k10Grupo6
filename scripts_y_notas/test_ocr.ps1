[Windows.Media.Ocr.OcrEngine, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if ($null -ne $engine) {
    Write-Output "Windows OCR is available! Language: $($engine.RecognizerLanguage.DisplayName)"
} else {
    Write-Output "Windows OCR is not available"
}
