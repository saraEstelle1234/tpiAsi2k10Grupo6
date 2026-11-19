# OCR script using Windows.Media.Ocr
Add-Type -AssemblyName System.Drawing
[Windows.Media.Ocr.OcrEngine, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null

function Run-OcrOnFile($imagePath, $outputJson) {
    $fullPath = (Resolve-Path $imagePath).Path
    $file = [Windows.Storage.StorageFile]::GetFileFromPathAsync($fullPath).GetAwaiter().GetResult()
    $stream = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read).GetAwaiter().GetResult()
    $decoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream).GetAwaiter().GetResult()
    $softwareBitmap = $decoder.GetSoftwareBitmapAsync().GetAwaiter().GetResult()
    
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
    $ocrResult = $engine.RecognizeAsync($softwareBitmap).GetAwaiter().GetResult()
    
    $lines = @()
    foreach ($line in $ocrResult.Lines) {
        $words = @()
        foreach ($w in $line.Words) {
            $words += @{
                text = $w.Text
                x = $w.BoundingRect.X
                y = $w.BoundingRect.Y
                w = $w.BoundingRect.Width
                h = $w.BoundingRect.Height
            }
        }
        $lines += @{
            text = $line.Text
            words = $words
        }
    }
    
    $result = @{
        image = $imagePath
        width = $decoder.PixelWidth
        height = $decoder.PixelHeight
        lines = $lines
    }
    
    $result | ConvertTo-Json -Depth 5 | Set-Content -Path $outputJson -Encoding UTF8
    Write-Output "OCR finished for $imagePath -> $outputJson ($($lines.Count) lines)"
}

Run-OcrOnFile "scripts_y_notas/extracted_dcu_full.png" "scripts_y_notas/ocr_dcu.json"
Run-OcrOnFile "scripts_y_notas/extracted_dcd_full.png" "scripts_y_notas/ocr_dcd.json"
