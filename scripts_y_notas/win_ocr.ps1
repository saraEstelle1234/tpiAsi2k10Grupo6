Add-Type -AssemblyName System.Drawing
[Windows.Globalization.Language,Windows.Globalization,ContentType=WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder,Windows.Graphics.Imaging,ContentType=WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine,Windows.Media.Ocr,ContentType=WindowsRuntime] | Out-Null

function Run-Ocr($imagePath) {
    Write-Host "=== OCR FOR: $imagePath ==="
    $file = [System.IO.Path]::GetFullPath($imagePath)
    $asyncOp = [Windows.Storage.StorageFile]::GetFileFromPathAsync($file)
    $storageFile = $asyncOp.GetAwaiter().GetResult()
    
    $streamOp = $storageFile.OpenAsync([Windows.Storage.FileAccessMode]::Read)
    $randomStream = $streamOp.GetAwaiter().GetResult()
    
    $decoderOp = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($randomStream)
    $decoder = $decoderOp.GetAwaiter().GetResult()
    
    $bitmapOp = $decoder.GetSoftwareBitmapAsync()
    $softwareBitmap = $bitmapOp.GetAwaiter().GetResult()
    
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
    if ($engine -eq $null) {
        $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new("es"))
    }
    if ($engine -eq $null) {
        $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new("en-US"))
    }
    
    $ocrOp = $engine.RecognizeAsync($softwareBitmap)
    $ocrResult = $ocrOp.GetAwaiter().GetResult()
    
    foreach ($line in $ocrResult.Lines) {
        Write-Host $line.Text
    }
}

Run-Ocr "media_presentacion/page_3_img_0_16.png"
Run-Ocr "media_presentacion/page_7_img_0_26.png"
Run-Ocr "media_presentacion/page_8_img_0_29.png"
