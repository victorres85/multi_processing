from multiprocessing import Event, Queue
from multiprocessing.managers import BaseManager
from queue import Empty
from typing import Any, List

from .debugging import app_logger as log


class QueueWrapper(object):
    def __init__(self, name: str, q: Queue = None, prevent_writes: Event = None): # type: ignore
        self.name = name
        self.q = q or Queue()
        self._prevent_writes = prevent_writes or Event()

    def get(self) -> Any:
        '''
        This call  blocks until it gets a message from the queue.
        '''
        if self.is_drained:
            return 'STOP'
        
        try:
            return self.q.get()
        except:
            log.info('q.get() interrupted')
            return 'STOP'

    def put(self, obj: object):
        ''' Used to add messages to the queue'''
        if self.is_writtable:
            log.debug('adding message to queue')
            self.q.put(obj)

    def put_many(self, objs: List[object]):
        ''' Used to pass messages to the put method'''
        for obj in objs:
            self.put(obj)
        

    def prevent_writes(self):
        '''
        Prevent external writes to the queue.
        This is useful for shutting down, or dealing with back pressure.
        '''
        log.debug(f'preventing writes to {self.name} queue')
        self._prevent_writes.set()

    @property
    def is_writtable(self)-> bool:
        '''
        Read-only property indicating if the queue is writable.
        '''
        return not self._prevent_writes.is_set()
    
    @property
    def is_drained(self)-> bool:
        '''
        If the queue is not writable and is empty the queue is draining.
        '''
        return not self.is_writtable and self.empty
    
    @property
    def empty(self) -> bool:
        '''
        Read-only property indicating that the queue is empty
        '''
        return self.q.empty()
    

class QueueManager(BaseManager):
    pass

def register_manager(name: str, queue: QueueManager = None):
    if queue:
        QueueManager.register(name, callable=lambda: queue)
    else:
        QueueManager.register(name)

def create_queue_manager(port: int) -> QueueManager:
    '''
    Binds to 127.0.0.1 on the given port.
    Using localhost on at least Debian systems results in extremly slow put() calls.
    '''
    return QueueManager(address=('127.0.0.1', port), authkey=b'ingestbackend')