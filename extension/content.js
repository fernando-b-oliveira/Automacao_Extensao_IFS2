/**
 * Web Data Bridge - Content Script Exemplo
 * Demonstra a captura genérica de elementos estruturados e envio assíncrono para o companion local.
 */
(() => {
  const BRIDGE_ENDPOINT = 'http://127.0.0.1:5000/api/v1/export';

  async function sendToLocalBridge(collectionName, records) {
    try {
      const response = await fetch(BRIDGE_ENDPOINT, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          collection: collectionName,
          records: records
        })
      });

      const data = await response.json();
      console.log('[Data Bridge] Resposta do servidor:', data);
      return data;
    } catch (err) {
      console.warn('[Data Bridge] Falha ao conectar ao servidor local:', err.message);
      throw err;
    }
  }

  // Exemplo de exposição no contexto global para acionamento controlado
  window.DataBridge = {
    exportDataset: sendToLocalBridge
  };

  console.log('[Data Bridge] Módulo carregado e pronto para exportação.');
})();
