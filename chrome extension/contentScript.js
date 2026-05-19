function downloadBlobAsFile(blob){
    const fileURL=URL.createObjectURL(blob);
    const downloadLink=document.createElement('a');
    downloadLink.href=fileURL;
    downloadLink.download='export.csv';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

async function fetchA(keyword) {
    const url="http://127.0.0.1:5000/analyze";
    try {
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({keyword: keyword}),
            headers: {
                "Content-Type": "application/json"
            }
        });
        if (!response.ok) {
            throw new Error(`Response Status: ${response.status}`);
        }
        const result = await response.blob();
        downloadBlobAsFile(result);
    } catch(error) {
        console.error(error.message);
    }
}

async function main(keyword){
    await fetchA(keyword)
}

const keyword=new URL(window.location.href).searchParams.get('keywords')
main(keyword);