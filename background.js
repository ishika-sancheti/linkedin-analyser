chrome.runtime.onMessage.addListener(
    (message)=>{
        const dataUrl="data:text/csv;charset=utf-8," + encodeURIComponent(message.csvText)
        chrome.downloads.download({url: dataUrl, filename: "export.csv", saveAs: false})
    }
)